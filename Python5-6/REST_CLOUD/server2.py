from flask import Flask, json, request, render_template
import random
import os
import dbclient as db 
import sys

api = Flask(__name__)
mydb = db.connect()
if mydb is None:
    print("Errore connessione al DB")
    sys.exit
            
def login_interno(user: dict):
    # usa il dizionario creato dal client.py
    for key, value in user.items():
        # usa una query
        sQuery = f"select privilegi from utenti where nomeutente = '{key}' and password = '{value}'"
        # richiamo la funzione scirtta in dbclient dove db e query
        NumeroRecords = db.read_in_db(mydb,sQuery)
        # se la query interrogta sul db è vera 
        if NumeroRecords == 1:
            print ("Login interno OK !")
            return True
    print("login interno KO")
    return False 
        

def controllo_privilegi_admin(user: dict):
   for key, value in user.items():
            sQuery = f"select privilegi from utenti where nomeutente = '{key}' and password = '{value[0]}'"
            #iNumRecord = db.read_in_db(mydb,sQuery)
            lRecord = db.read_next_row(mydb)
            iStato = lRecord[1][0]
            #print("Stampo lo stato")
            #print(iStato)
            if iStato == '1':
                #print("controllo ok")
                return True
            else:
                #print("controllo ko")
                
                return False

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        print(dati)

        if login_interno(accesso) and controllo_privilegi_admin(accesso):

            for key , value in dati.items():
                codiceFiscale = key
                nome = value['nome']
                cognome = value['cognome']
                dataNascita = value['dataNascita']
                sQuery = f"insert into cittadini(nome, cognome, data_nascita, codice_fiscale) values ('{nome}', '{cognome}', '{dataNascita}', '{key}')"
                print(sQuery)
                iRetValue = db.write_in_db(mydb,sQuery)
                if iRetValue == -2:
                    return "Nome utente già in uso"
                elif iRetValue == 0:
                    return "Inserimento avvenuto con successo"
                else:
                    return "Errore non gestito nella registrazione"
        return "Richiesta non conforme"
    else:
        return "Content-Type not supported!"

    
    
@api.route('/read_cittadino', methods=['POST'])
def GestisciReadCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if login_interno(accesso):
            with open("anagrafe.json") as json_file:
                cittadini = json.load(json_file)
            for key, value in cittadini.items():
                if dati == key:
                    return cittadini[key]
            return "Cittadino non trovato"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
@api.route('/update_cittadino', methods=['POST'])
def GestisciUpdateCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if login_interno(accesso) and controllo_privilegi_admin(accesso):
            with open("anagrafe.json") as json_file:
                cittadini = json.load(json_file)
        
            if dati[0] not in cittadini:
                return "Errore, codice fiscale non trovato"

            for i in range(len(dati) - 1):
                if dati[i+1]:
                    if i + 1 == 1:
                        cittadini[dati[0]]["cognome"] = dati[i+1]
                    elif i + 1 == 2:
                        cittadini[dati[0]]["dataNascita"] = dati[i+1]
                    elif i + 1 == 3:
                        cittadini[dati[0]]["nome"] = dati[i+1]
            with open("anagrafe.json", "w") as json_file:
                json.dump(cittadini, json_file)
            return "Modifica avvenuta con successo"   
        else:
            return "Dati errati"     
    else:
        return 'Content-Type not supported!'

@api.route('/delete_cittadino', methods=['POST'])
def GestisciDeleteCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if login_interno(accesso) and controllo_privilegi_admin(accesso):
            with open("anagrafe.json") as json_file:
                cittadini = json.load(json_file)
        
            if dati not in cittadini:
                return "Errore, codice fiscale non trovato"
            cittadini.pop(dati)
            with open("anagrafe.json", "w") as json_file:
                json.dump(cittadini, json_file)
                
            return "Eliminazione avvenuta con successo"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
@api.route('/login', methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
       
        iStato = -1
        for key, value in request.json.items():
            sQuery = f"select privilegi from utenti where nomeutente = '{key}' and password = '{value[0]}'"
            iNumRecord = db.read_in_db(mydb,sQuery)
            if iNumRecord == 1:
                print("Login terminato correttamente")
                lRecord = db.read_next_row(mydb)
                iStato = lRecord[1][0]
                return '{"Esito":"ok","Stato" : '+ str(iStato)+'}'
            elif iNumRecord == 0:
                print("Credenziali errate")
                return '{"Esito":"ko","Stato": -1}'
            elif iNumRecord <= -1:
                print("Dati Errati")
                sContent = "{'Esito':'ok','Stato':-1}"
                return sContent
            else:
                print("Attenzione: attacco in corso")
                return "{'Esito':'ko','Stato':-1}"
    else:
        return 'Content-Type not supported!'
    

@api.route('/registrazione', methods=['POST'])
def Registrazione():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        #Dobbiamo intervenire qui
        #dobbiamo verificare se lo username è già presente nella tabella
        #altrimenti facciamo la insert
        for key , value in request.json.items():
            sQuery = f"insert into utenti(nomeutente,password,privilegi) values ('{key}', '{value[0]}', {random.randint(0,1)})"
            print(sQuery)
            iRetValue = db.write_in_db(mydb,sQuery)
            if iRetValue == -2:
                return "Nome utente già in uso"    
            elif iRetValue == 0:
              return "Registrazione avvenuta con successo"
            else:
                return "Errore non gestito nella registrazione"
        return "Richiesta non conforme"
    else:
        return "Content-Type not supported!"



api.run(host="127.0.0.1", port=8080, ssl_context='adhoc')
