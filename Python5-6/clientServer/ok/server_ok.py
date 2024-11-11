from flask import Flask, jsonify, request
from myjson import JsonDeserialize, JsonSerialize

api = Flask(__name__)


file_path = "anagrafe.json"
cittadini = JsonDeserialize(file_path)

utenti = {
    "admin": {"password": "admin123", "privilegio": "write"},  
    "utente_normale": {"password": "password123", "privilegio": "read"} 
}

# Per la gestione delle credenziali
@api.route('/Gestisci_Credenziali', methods=['POST'])
def Gestisci_Credenziali():
    content_type = request.headers.get('Content-Type')
    
    # Controlliamo che il contenuto sia JSON
    if content_type == 'application/json':
        jsonReq = request.json
        username = jsonReq.get("username")
        password = jsonReq.get("password")
        
        # Controlla se l'username esiste e se la password corrisponde
        if username in utenti and utenti[username]["password"] == password:
            privilegio = utenti[username]["privilegio"]  # Recupera il privilegio
            return jsonify({"Esito": "200", "Msg": "Autenticazione riuscita", "privilegio": privilegio}), 200
        else:
            return jsonify({"Esito": "401", "Msg": "Autenticazione fallita: username o password errati"}), 401
    else:
        return jsonify({"Esito": "400", "Msg": "Content-Type non supportato, deve essere application/json"}), 400

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        codice_fiscale = jsonReq.get('codFiscale')
        if codice_fiscale in cittadini:
            return jsonify({"Esito": "200", "Msg": "Cittadino già esistente"}), 200
        else:
            cittadini[codice_fiscale] = jsonReq
            JsonSerialize(cittadini, file_path) 
            return jsonify({"Esito": "200", "Msg": "Cittadino aggiunto con successo"}), 200
    else:
        return 'Content-Type non supportato!'

@api.route('/read_cittadino/<codice_fiscale>', methods=['GET'])
def read_cittadino(codice_fiscale):
    cittadino = cittadini.get(codice_fiscale)
    if cittadino:
        return jsonify({"Esito": "200", "Msg": "Cittadino trovato", "Dati": cittadino}), 200
    else:
        return jsonify({"Esito": "404", "Msg": "Cittadino non trovato"}), 404

@api.route('/update_cittadino', methods=['POST'])
def update_cittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        codice_fiscale = jsonReq.get('codFiscale')
        if codice_fiscale in cittadini:
            cittadini[codice_fiscale] = jsonReq
            JsonSerialize(cittadini, file_path)  
            return jsonify({"Esito": "200", "Msg": "Cittadino aggiornato con successo"}), 200
        else:
            return jsonify({"Esito": "404", "Msg": "Cittadino non trovato"}), 404
    else:
        return 'Content-Type non supportato!'

@api.route('/elimina_cittadino', methods=['POST'])
def elimina_cittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        cod = request.json.get('codFiscale')
        if cod in cittadini:
            del cittadini[cod]
            JsonSerialize(cittadini, file_path)  
            return jsonify({"Esito": "200", "Msg": "Cittadino rimosso con successo"}), 200
        else:
            return jsonify({"Esito": "404", "Msg": "Cittadino non trovato"}), 404
    else:
        return 'Content-Type non supportato!'

#api.run(host="127.0.0.1", port=8080)
api.run(host="127.0.0.1", port=8080, ssl_context = 'adhoc')

