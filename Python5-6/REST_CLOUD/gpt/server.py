from flask import Flask, request
import random
import dbclient as db
import sys

api = Flask(__name__)
mydb = db.connect()
if mydb is None:
    print("Errore connessione al DB")
    sys.exit()

def login_interno(user: dict):
    for key, value in user.items():
        sQuery = f"SELECT privilegi FROM utenti WHERE nomeutente = '{key}' AND password = '{value}'"
        NumeroRecords = db.read_in_db(mydb, sQuery)
        if NumeroRecords == 1:
            print("Login interno OK!")
            return True
    print("Login interno KO")
    return False

def controllo_privilegi_admin(user: dict):
    for key, value in user.items():
        sQuery = f"SELECT privilegi FROM utenti WHERE nomeutente = '{key}' AND password = '{value[0]}'"
        db.read_in_db(mydb, sQuery)
        lRecord = db.read_next_row(mydb)
        iStato = lRecord[1][0]
        if iStato == '1':
            return True
        else:
            return False

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        accesso = request.json[1]
        dati = request.json[0]

        if login_interno(accesso) and controllo_privilegi_admin(accesso):
            for key, value in dati.items():
                codiceFiscale = key
                nome = value['nome']
                cognome = value['cognome']
                dataNascita = value['dataNascita']
                sQuery = f"INSERT INTO cittadini(nome, cognome, data_nascita, codice_fiscale) VALUES ('{nome}', '{cognome}', '{dataNascita}', '{codiceFiscale}')"
                iRetValue = db.write_in_db(mydb, sQuery)
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
    if content_type == 'application/json':
        accesso = request.json[1]
        dati = request.json[0]
        if login_interno(accesso):
            sQuery = f"SELECT * FROM cittadini WHERE codice_fiscale = '{dati}'"
            db.read_in_db(mydb, sQuery)
            cittadino = db.read_next_row(mydb)
            if cittadino:
                return {
                    "nome": cittadino[1],
                    "cognome": cittadino[2],
                    "dataNascita": cittadino[3],
                    "codiceFiscale": cittadino[4]
                }
            return "Cittadino non trovato"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'

@api.route('/update_cittadino', methods=['POST'])
def GestisciUpdateCittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        accesso = request.json[1]
        dati = request.json[0]
        if login_interno(accesso) and controllo_privilegi_admin(accesso):
            codiceFiscale = dati[0]
            nome = dati[3] if dati[3] else None
            cognome = dati[1] if dati[1] else None
            dataNascita = dati[2] if dati[2] else None

            if nome:
                db.write_in_db(mydb, f"UPDATE cittadini SET nome = '{nome}' WHERE codice_fiscale = '{codiceFiscale}'")
            if cognome:
                db.write_in_db(mydb, f"UPDATE cittadini SET cognome = '{cognome}' WHERE codice_fiscale = '{codiceFiscale}'")
            if dataNascita:
                db.write_in_db(mydb, f"UPDATE cittadini SET data_nascita = '{dataNascita}' WHERE codice_fiscale = '{codiceFiscale}'")
            
            return "Modifica avvenuta con successo"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'

@api.route('/delete_cittadino', methods=['POST'])
def GestisciDeleteCittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        accesso = request.json[1]
        dati = request.json[0]
        if login_interno(accesso) and controllo_privilegi_admin(accesso):
            db.write_in_db(mydb, f"DELETE FROM cittadini WHERE codice_fiscale = '{dati}'")
            return "Eliminazione avvenuta con successo"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
