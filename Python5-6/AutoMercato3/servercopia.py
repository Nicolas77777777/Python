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


@api.route('/add_automobile', methods=['POST'])
def GestisciAutomobile():

    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    
    if content_type == 'application/json':
        accesso = request.json[1]
        dati = request.json[0]
        
        print(f"Dati accesso: {accesso}")
        print(f"Dati automobile: {dati}")
        
        if controllo_privilegi_admin(accesso) == 1:
            print("Privilegi amministrativi confermati.")
            
            if isinstance(dati, dict):
                try:
                    sQuery = f"""
                    INSERT INTO automobili (marca, modello, colore, targa, magazzino_id, condizione, disponibilita)
                    VALUES (
                        '{dati['marca']}', 
                        '{dati['modello']}', 
                        '{dati['colore']}', 
                        '{dati['targa']}', 
                        {dati['magazzino_id']}, 
                        '{dati['condizione']}', 
                        {dati['disponibilita']}
                    )
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

@api.route('/add_motocicletta', methods=['POST'])
def GestisciMotocicletta():

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
                    INSERT INTO motociclette (marca, modello, colore, targa, magazzino_id, condizione, disponibilita)
                    VALUES (
                        '{dati['marca']}', 
                        '{dati['modello']}', 
                        '{dati['colore']}', 
                        '{dati['targa']}', 
                        {dati['magazzino_id']}, 
                        '{dati['condizione']}', 
                        {dati['disponibilita']}
                    )
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

@api.route('/cerca_automobile', methods=['POST'])
def GestisciCercaAutomobile():
    # request richiesta è globale, headres intestazione.get 
    if request.headers.get('Content-Type') == 'application/json':
        try:

            dati = request.json
            criteri = dati.get('criteri', {})
            
            # Costruzione della query di base
            query = """
                SELECT a.*, f.nome AS filiale_nome, f.indirizzo AS filiale_indirizzo
                FROM automobili a
                JOIN filiali f ON a.magazzino_id = f.id
            """
            conditions = []

            # Aggiunta dinamica dei criteri
            if "marca" in criteri:
                conditions.append(f"a.marca = %s")#(f"a.marca = criteri.get("marca")) #%s per evitare sql injection 
            if "modello" in criteri:
                conditions.append(f"a.modello = %s") 
            if "colore" in criteri:
                conditions.append(f"a.colore = %s")
            if "condizione" in criteri:
                conditions.append(f"a.condizione = %s")
            # se l'utente  scirve alemno un valore 
            if conditions: # se è vera se la lista è vuota è false , è popolato 
                query += " WHERE "
                query += " AND ".join(conditions) # metodo  join prende un array lista , prende tutti i valori e li sostituisce con il valore tra "" in questo caso " and "

            # Creazione dei parametri per la query
            parameters = [
                criteri.get("marca"),
                criteri.get("modello"),
                criteri.get("colore"),
                criteri.get("condizione"),
            ]

            # filtro i parametri 
            filtered_parameters = []
            for p in parameters:
                if p is not None:
                    filtered_parameters.append(p)
            parameters = filtered_parameters

            # qui potrei controllare l'sql injection 
            
            # Connessione al database ho letto 
            cur = db.connect()
            # se la connesione non è andata a buon fine 
            if cur is None:
                return {"status": "error", "message": "Errore di connessione al database"}, 500 

            # Esecuzione della query
            cur.execute(query, tuple(parameters))
            # results è una lista di liste
            results = cur.fetchall() # fetchall prendere e raccogliere li prende e li tiene in canna 

            # Creazione del risultato in formato JSON
            data = [
                {
                    "id": auto[0],
                    "marca": auto[1],
                    "modello": auto[2],
                    "colore": auto[3],
                    "targa": auto[4],
                    "magazzino_id": auto[5],
                    "condizione": auto[6],
                    "disponibilita": auto[7],
                    "filiale_nome": auto[8],
                    "filiale_indirizzo": auto[9],
                    
                    # "marca": auto[0],
                    # "modello": auto[1],
                    # "colore": auto[2],
                    # "targa": auto[3],
                    # "magazzino_id": auto[4],
                    # "condizione": auto[5],
                    # "disponibilita": auto[6],
                    # "filiale_nome": auto[7],
                    # "filiale_indirizzo": auto[8],
                }
                for auto in results
            ]

            if data:
                return {"status": "success", "data": data}, 200
            else:
                return {"status": "success", "message": "Nessuna automobile trovata per i criteri specificati"}, 404

        except Exception as e:
            return {"status": "error", "message": str(e)}, 500

    return {"status": "error", "message": "Content-Type non supportato!"}, 400


    
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