from flask import Flask, json, request, render_template
import random
import os
import dbclient as db
import urllib3

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


@api.route('//add_immobile_affitto', methods=['POST'])
def GestisciAddImmobileAffitto():
   
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    
    if content_type == 'application/json':
        try:
            accesso = request.json[1]
            dati = request.json[0]
            
            print(f"Dati accesso: {accesso}")
            print(f"Dati Immobile: {dati}")
            
            if controllo_privilegi_admin(accesso) == 1:
                print("Privilegi amministrativi confermati.")
                
                if isinstance(dati, dict):
                    # Creazione della query SQL
                    sQuery = f"""
                    INSERT INTO case_in_affitto (catastale, indirizzo, civico, tipo_affitto, bagno_personale, prezzo_mensile, filiale_proponente)
                    VALUES (
                        '{dati['catastale']}',
                        '{dati['indirizzo']}',
                        {dati['civico']},
                        '{dati['tipo_affitto']}',
                        {'TRUE' if dati['bagno_personale'] else 'FALSE'},
                        {dati['prezzo_mensile']},
                        '{dati['filiale_proponente']}'
                    );
                    """
                    print(f"Esecuzione query: {sQuery}")
                    iRetValue = db.write_in_db(mydb, sQuery)
                    
                    if iRetValue == -2:
                        return "Codice catastale già esistente", 409
                    elif iRetValue == 0:
                        return "Immobile in affitto aggiunto con successo", 200
                    else:
                        return "Errore non gestito nella registrazione", 500
                else:
                    print("Formato non valido per 'dati'")
                    return "Errore: formato dati non valido", 400
            else:
                print("Privilegi amministrativi non confermati.")
                return "Dati errati", 403
        except Exception as e:
            print(f"Errore durante l'inserimento nel database: {e}")
            return f"Errore interno del server: {e}", 500
    else:
        return 'Content-Type not supported!', 415

@api.route('/add_immobile_vendita', methods=['POST'])
def GestisciAddImmobileVendita():

    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    
    if content_type == 'application/json':
        accesso = request.json[1]
        dati = request.json[0]
        
        print(f"Dati accesso: {accesso}")
        print(f"Dati Motocilcetta: {dati}")
        
        if controllo_privilegi_admin(accesso) == 1:
            print("Privilegi amministrativi confermati.")
            
            if isinstance(dati, dict):
                try:
                    sQuery = f"""
        INSERT INTO case_in_vendita (catastale, indirizzo, numero_civico, piano, metri, vani, prezzo, stato, filiale_proponente)
        VALUES (
            '{dati['catastale']}',
            '{dati['indirizzo']}',
            {dati['numero_civico']},
            {dati['piano'] if dati['piano'] is not None else 'NULL'},
            {dati['metri']},
            {dati['vani']},
            {dati['prezzo']},
            '{dati['stato']}',
            '{dati['filiale_proponente']}'
        );
        """
                    print(f"Esecuzione query: {sQuery}")
                    iRetValue = db.write_in_db(mydb, sQuery)
                    
                    if iRetValue == -2:
                        return "Targa già esistente"
                    elif iRetValue == 0:
                        return "Registrazione avvenuta con successo"
                    else:
                        return "Errore non gestito nella registrazione"
                except Exception as e:
                    print(f"Errore durante l'inserimento nel database: {e}")
                    return "Errore interno del server"
            else:
                print("Formato non valido per 'dati'")
                return "Errore: formato dati non valido"
        else:
            print("Privilegi amministrativi non confermati.")
            return "Dati errati"
    else:
        return 'Content-Type not supported!'

@api.route('/cerca_immobile_vendita', methods=['POST'])
def CercaImmobileVendita():
    """
    Gestisce la ricerca degli immobili in vendita basandosi sui criteri forniti dal client.
    """
    if request.headers.get('Content-Type') == 'application/json':
        try:
            dati = request.json
            criteri = dati.get('criteri', {})

            # Costruzione della query di base
            query = """
                SELECT 
                    catastale, indirizzo, numero_civico, piano, metri, vani, prezzo, stato, filiale_proponente
                FROM 
                    case_in_vendita
            """
            conditions = []

            # Aggiunta dinamica dei criteri
            if "piano" in criteri:
                conditions.append("piano = %s")
            if "metri" in criteri:
                conditions.append("metri = %s")
            if "vani" in criteri:
                conditions.append("vani = %s")
            if "prezzo" in criteri:
                conditions.append("prezzo <= %s")
            if "stato" in criteri:
                conditions.append("stato = %s")

            # Aggiungi condizioni alla query se ci sono criteri
            if conditions:
                query += " WHERE " + " AND ".join(conditions)

            # Creazione dei parametri per la query
            parameters = [
                criteri.get("piano"),
                criteri.get("metri"),
                criteri.get("vani"),
                criteri.get("prezzo"),
                criteri.get("stato"),
            ]
            # Rimuovi i valori None dai parametri
            parameters = [p for p in parameters if p is not None]

            # Connessione al database
            cur = db.connect()
            if cur is None:
                return {"status": "error", "message": "Errore di connessione al database"}, 500

            # Esecuzione della query
            cur.execute(query, tuple(parameters))
            results = cur.fetchall()

            # Creazione del risultato in formato JSON
            data = [
                {
                    "catastale": immobile[0],
                    "indirizzo": immobile[1],
                    "numero_civico": immobile[2],
                    "piano": immobile[3],
                    "metri": immobile[4],
                    "vani": immobile[5],
                    "prezzo": immobile[6],
                    "stato": immobile[7],
                    "filiale_proponente": immobile[8],
                }
                for immobile in results
            ]

            if data:
                return {"status": "success", "data": data}, 200
            else:
                return {"status": "success", "message": "Nessun immobile trovato per i criteri specificati"}, 404

        except Exception as e:
            return {"status": "error", "message": str(e)}, 500

    return {"status": "error", "message": "Content-Type non supportato!"}, 400


    
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
            sQuery = f"INSERT INTO utenti(username, pass, stato) VALUES ('{key}', '{value[0]}', {random.randint(0,1)})"

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