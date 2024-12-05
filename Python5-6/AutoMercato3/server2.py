from flask import Flask, json, request, render_template
import random
import os
import dbclient as db
import sys

api = Flask(__name__)
mydb = db.connect()
if mydb is None:
    print("Errore connessione al DB")
    sys.exit()
    
@api.route('/')
def home():
    return render_template('home.html')

@api.route('/login-page', methods=['GET'])
def loginPage():
    return render_template('login.html')

@api.route('/new-automobile', methods=['GET'])
def newAutomobile():
    return render_template('new-automobile.html')


@api.route('/login-action', methods=['POST'])
def loginAction():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    #if (content_type == 'application/json'):
    sUsername = request.form.get("username")
    sPassword = request.form.get("password")
    sRisposta = "Ciao mi hai mandato " + sUsername + " insieme a " + sPassword
    #return "<html><body>" + sRisposta + "</body></html>"

    sQuery = f"select * from utenti where username = {sUsername} and password = '{sPassword}';"
    iNumRecord = db.read_in_db(mydb, sQuery)
    if iNumRecord == 1:
        print("Login terminato correttamente")
        lRecord = db.read_next_row(mydb)
        iStato = lRecord[1][0]
        return '{"Esito":"ok", "Stato": ' + str(iStato) + '}'
    elif iNumRecord == 0:
        print("Credenziali errate")
        return '{"Esito":"ko", "Stato": ' + str(iStato) + '}'
    elif iNumRecord <= -1:
        print("Dati errati")
        return '{"Esito":"ko", "Stato": ' + str(iStato) + '}'
    else:
        print("Attenzione: attacco in corso")
        return '{"Esito":"ko", "Stato": ' + str(iStato) + '}'
    


# @api.route('/login-action123', methods=['POST'])
# def loginAction123():
#     content_type = request.headers.get('Content-Type')
#     print("Ricevuta chiamata " + content_type)
#     if (content_type == 'application/json'):
#         iStato = -1
#         for key, value in request.json.items():
#             sQuery = f"select privilegi from utente where username = '{key}' and password = '{value[0]}';"
#             print(sQuery)
#             iNumRecord = db.read_in_db(mydb, sQuery)
#             if iNumRecord == 1:
#                 print("Login terminato correttamente")
#                 lRecord = db.read_next_row(mydb)
#                 iStato = lRecord[1][0]
#                 return '{"Esito":"ok", "Stato": ' + str(iStato) + '}'
#             elif iNumRecord == 0:
#                 print("Credenziali errate")
#                 return '{"Esito":"ko", "Stato": ' + str(iStato) + '}'
#             elif iNumRecord <= -1:
#                 print("Dati errati")
#                 return '{"Esito":"ko", "Stato": ' + str(iStato) + '}'
#             else:
#                 print("Attenzione: attacco in corso")
#                 return '{"Esito":"ko", "Stato": ' + str(iStato) + '}'
#     else:
#         message = "Content Type not supported"
#         #return 'Content-Type not supported!'
#         return api.redirect("/login-page",message)

def controllo_privilegi_admin(user: dict):
    for key, value in user.items():
        sQuery = f"select privilegi from utente where username = '{key}' and password = '{value[0]}';"
        print(sQuery)
        iNumRecord = db.read_in_db(mydb, sQuery)
        if iNumRecord == 1:
            lRecord = db.read_next_row(mydb)
            iStato = lRecord[1][0]
            return iStato
        return False

@api.route('/add_automobile', methods=['POST'])
def GestisciAddAutomobile():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if controllo_privilegi_admin(accesso) == 1:
            for key, value in dati.items():
                sQuery = f"insert into automobile(marca, modello, colore, posizione, filiale_id, condizione) values ('{dati['marca']}', '{dati['modello']}', '{dati['colore']}', '{dati['posizione']}', '{dati['filiale_id']}', '{dati['condizione']}')"
                iRetValue = db.write_in_db(mydb,sQuery)
                if iRetValue == -2:
                    return "Automobile già esistente"
                elif iRetValue == 0:
                    return "Registrazione avvenuta con successo"
                else:
                    return "Errore non gestito nella registrazione"
            return "Errore richiesta non conforme"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
    
@api.route('/read_automobile', methods=['POST'])
def GestisciReadAutomobile():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if controllo_privilegi_admin(accesso) == 1 or controllo_privilegi_admin(accesso) == 0:
        
            sQuery = f"select * from automobile where marca = '{dati['marca']}' and modello = '{dati['modello']}' and colore = '{dati['colore']}' and condizione = '{dati['condizione']}'"
            iRetValue = db.read_in_db(mydb,sQuery)
            if iRetValue == 1:
                sValue = db.read_next_row(mydb)
                return f'{sValue}'
            return "Automobile non trovata"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
@api.route('/vendita_automobile', methods=['POST'])
def GestisciVendita():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if controllo_privilegi_admin(accesso) == 1:

            with open("auto_vendute.json", "w") as file:
                json.dump([dati], file, indent=4)

            print("File creato con la prima auto venduta!")

            try:
                with open("auto_vendute.json", "r") as file:
                    auto_vendute = json.load(file)
            except FileNotFoundError:
                
        # Se il file non esiste, inizializza una lista vuota
                auto_vendute = []

        # Aggiungi la nuova auto alla lista
            auto_vendute.append(dati)

        # Salva di nuovo i dati aggiornati nel file JSON
            with open("auto_vendute.json", "w") as file:
                json.dump(auto_vendute, file, indent=4)

            print("Nuova auto aggiunta con successo!")
            return "Registrazione avvenuta con successo"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'


@api.route('/delete_automobile', methods=['POST'])
def GestisciDeleteAutomobile():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if controllo_privilegi_admin(accesso) == 1:
            sQuery = f"delete from automobile where id = '{dati}'"
            iRetValue = db.write_in_db(mydb,sQuery)
            if iRetValue == -2:
                return "Automobile non esistente"
            elif iRetValue == 0:
                return "Eliminazione avvenuta con successo"
            else:
                return "Errore non gestito nella registrazione"                
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
            

    

@api.route('/login', methods=['POST'])
def login1():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        iStato = -1
        for key, value in request.json.items():
            sQuery = f"select privilegi from utente where username = '{key}' and password = '{value[0]}';"
            print(sQuery)
            iNumRecord = db.read_in_db(mydb, sQuery)
            if iNumRecord == 1:
                print("Login terminato correttamente")
                lRecord = db.read_next_row(mydb)
                iStato = lRecord[1][0]
                return '{"Esito":"ok", "Stato": ' + str(iStato) + '}'
            elif iNumRecord == 0:
                print("Credenziali errate")
                return '{"Esito":"ko", "Stato": ' + str(iStato) + '}'
            elif iNumRecord <= -1:
                print("Dati errati")
                return '{"Esito":"ko", "Stato": ' + str(iStato) + '}'
            else:
                print("Attenzione: attacco in corso")
                return '{"Esito":"ko", "Stato": ' + str(iStato) + '}'
    else:
        return 'Content-Type not supported!'

@api.route('/registrazione', methods=['POST'])
def Registrazione():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        for key, value in request.json.items():
            sQuery = f"insert into utente(username,password,privilegi) values ('{key}', '{value[0]}',{random.randint(0,1)})"
            print(sQuery)
            iRetValue = db.write_in_db(mydb, sQuery) #restituisce 0 se è andato tutto bene, -1 errore, -2 duplicate key
            print(iRetValue)
            if iRetValue == -2:
                return "Nome utente già in uso"
            elif iRetValue == 0:
                return "Registrazione avvenuta con successo"
            else:
                return "Errore non gestito nella registrazione"
        return "Errore richiesta non conforme"
    else:
        return 'Content-Type not supported!'

#api.run(host="127.0.0.1", port=8080, ssl_context='adhoc')   
api.run(host="127.0.0.1", port=8080)  