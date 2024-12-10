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
        sQuery = f"SELECT stato FROM utenti WHERE username = '{key}' AND pass = '{value[0]}';"
        print(f"Query eseguita: {sQuery}")
        iNumRecord = db.read_in_db(mydb, sQuery)
        print(f"Numero di record trovati: {iNumRecord}")
        if iNumRecord == 1:
            lRecord = db.read_next_row(mydb)
            print(f"Record letto: {lRecord}")
            iStato = int(lRecord[1][0])  # Convertiamo il valore in intero
            print(f"Valore di stato: {iStato}")
            return iStato
        return False



@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if content_type == 'application/json':
        accesso = request.json[1]
        dati = request.json[0]
        print(f"Dati accesso: {accesso}")
        print(f"Dati cittadino: {dati}")
        if controllo_privilegi_admin(accesso) == 1:
            print("Privilegi amministrativi confermati.")
            for key, value in dati.items():
                sQuery = f"""
                INSERT INTO cittadini (codice_fiscale, nome, cognome, data_nascita, comune_residenza)
                VALUES ('{key}', '{value['nome']}', '{value['cognome']}', '{value['dataNascita']}', '{value['comuneResidenza']}')
                """
                print(f"Esecuzione query: {sQuery}")
                iRetValue = db.write_in_db(mydb, sQuery)
                if iRetValue == -2:
                    return "Codice fiscale già esistente"
                elif iRetValue == 0:
                    return "Registrazione avvenuta con successo"
                else:
                    return "Errore non gestito nella registrazione"
            return "Errore richiesta non conforme"
        else:
            print("Privilegi amministrativi non confermati.")
            return "Dati errati"
    else:
        return 'Content-Type not supported!'

    
@api.route('/read_cittadino', methods=['POST'])
def GestisciReadCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if controllo_privilegi_admin(accesso) == 1 or controllo_privilegi_admin(accesso) == 0:
            sQuery = f"select * from cittadini where codice_iscale = '{dati}'"
            iRetValue = db.read_in_db(mydb,sQuery)
            if iRetValue == 1:
                sValue = db.read_next_row(mydb)
                return sValue
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
        if controllo_privilegi_admin(accesso) == 1:
            sQuery = f"select * from cittadini where codice_fiscale = '{dati[0]}'"
            iRetValue = db.read_in_db(mydb,sQuery)
            if iRetValue != 1:
                return "Cittadino non trovato"

            for i in range(len(dati) - 1):
                if dati[i+1]:
                    if i + 1 == 1:
                        sQuery = f"update cittadini set cognome = '{dati[i+1]}' where codice_fiscale= '{dati[0]}'"
                        db.write_in_db(mydb,sQuery)
                    elif i + 1 == 2:
                        sQuery = f"update cittadini set dataN = '{dati[i+1]}' where codice_fiscale = '{dati[0]}'"
                        db.write_in_db(mydb,sQuery)
                    elif i + 1 == 3:
                        sQuery = f"update cittadini set nome = '{dati[i+1]}' where codice_fiscale = '{dati[0]}'"
                        db.write_in_db(mydb,sQuery)
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
        if controllo_privilegi_admin(accesso) == 1:
            sQuery = f"delete from cittadini where codice_fiscale = '{dati}'"
            iRetValue = db.write_in_db(mydb,sQuery)
            if iRetValue == -2:
                return "Nome utente non esistente"
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
            sQuery = f"select stato from utenti where username = '{key}' and pass = '{value[0]}';"
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
            #sQuery = f"insert into utenti(username,pass,stato) values ('{key}', '{value[0]}',{random.randint(0,1)})"
            sQuery = f"INSERT INTO utenti(username, pass, stato, ruolo) VALUES ('{key}', '{value[0]}', {random.randint(0,1)}, 'user')"

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