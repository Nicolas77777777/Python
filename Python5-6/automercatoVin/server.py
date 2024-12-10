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
                sQuery = f"insert into automobile(num_telaio,marca, modello, colore, filiale, condizione) values ('{dati['num_telaio']}','{dati['marca']}', '{dati['modello']}', '{dati['colore']}', '{dati['filiale']}', '{dati['condizione']}')"
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
            """with open("anagrafe.json") as json_file:
                cittadini = json.load(json_file)
            for key, value in cittadini.items():
                if dati == key:
                    return cittadini[key]
            return "Cittadino non trovato"""
            lista = []
            sQuery = f"select * from automobile where marca = '{dati['marca']}' and modello = '{dati['modello']}' and colore = '{dati['colore']}' and condizione = '{dati['condizione']}'"
            iRetValue = db.read_in_db(mydb,sQuery)
            if iRetValue > 0:
                for ii in range(0,iRetValue):
                        sValue = db.read_next_row(mydb)
                        print(sValue[1])
                        lista.append(sValue[1])
                return f'{lista}'
            
            return "Automobile non trovata"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
# @api.route('/update_cittadino', methods=['POST'])
# def GestisciUpdateCittadino():
#     content_type = request.headers.get('Content-Type')
#     print("Ricevuta chiamata " + content_type)
#     if (content_type == 'application/json'):
#         accesso = request.json[1]
#         dati = request.json[0]
#         if controllo_privilegi_admin(accesso) == 1:
#             sQuery = f"select * from cittadini where codFisc = '{dati[0]}'"
#             iRetValue = db.read_in_db(mydb,sQuery)
#             if iRetValue != 1:
#                 return "Cittadino non trovato"

#             for i in range(len(dati) - 1):
#                 if dati[i+1]:
#                     if i + 1 == 1:
#                         sQuery = f"update cittadini set cognome = '{dati[i+1]}' where codFisc = '{dati[0]}'"
#                         db.write_in_db(mydb,sQuery)
#                     elif i + 1 == 2:
#                         sQuery = f"update cittadini set dataN = '{dati[i+1]}' where codFisc = '{dati[0]}'"
#                         db.write_in_db(mydb,sQuery)
#                     elif i + 1 == 3:
#                         sQuery = f"update cittadini set nome = '{dati[i+1]}' where codFisc = '{dati[0]}'"
#                         db.write_in_db(mydb,sQuery)
#             return "Modifica avvenuta con successo"   
#         else:
#             return "Dati errati"     
#     else:
#         return 'Content-Type not supported!'

@api.route('/vendita_automobile', methods=['POST'])
def GestisciVendita():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if controllo_privilegi_admin(accesso) == 1:
            
            sQuery = f" SELECT filiale, COUNT(*) AS numero_vendite FROM vendita_auto where data_vendita = '{dati['data']}' GROUP BY filiale ORDER BY numero_vendite DESC;"
            iRetValue = db.read_in_db(mydb,sQuery)
            lista = []
            if iRetValue > 0:
                for ii in range(0,iRetValue):
                        sValue = db.read_next_row(mydb)
                        print(sValue[1])
                        lista.append(sValue[1])
                return f'{lista}'
            
            return "Automobile non trovata"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
            
    #     try:
    #             with open("auto_vendute.json", "r") as file:
    #                 auto_vendute = json.load(file)
    #     except FileNotFoundError:
    #             return ("File non trovato")

    #     auto_vendute.append(dati)

    #     # Salva di nuovo i dati aggiornati nel file JSON
    #             with open("auto_vendute.json", "w") as file:
    #                 json.dump(auto_vendute, file, indent=4)

    #                 print("Nuova auto aggiunta con successo!")
    #                 return "Registrazione avvenuta con successo"
    #             else:
    #                 return "Dati errati"
    # else:
    #     return 'Content-Type not supported!'


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
def login():
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

api.run(host="127.0.0.1", port=8080, ssl_context='adhoc')   