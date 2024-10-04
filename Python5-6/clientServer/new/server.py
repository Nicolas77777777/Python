from flask import Flask, json, request
from myjson import JsonSerialize,JsonDeserialize

sAnagrafe = "./anagrafe.json"
privilegi = "./xxx.json"

api = Flask(__name__)

#mettere una lista di liste dove ogni lista è un cittadino

#la chiave è il codice fiscale
#add cittadino
#read cittadino
#update cittadino
#delete cittadino


# Per la gestione delle credenziali
@api.route('/Gestisci_Credenziali', methods=['POST'])
def Gestisci_Credenziali():
    content_type = request.headers.get('Content-Type')
    
    # Controlliamo che il contenuto sia JSON
    if content_type == 'application/json':
        jsonReq = request.json
        username = jsonReq.get("username")
        password = jsonReq.get("password")

        utenti =  JsonDeserialize(privilegi)
        if username in utenti and password == utenti[username]:
        # Controlla se l'username esiste e se la password corrisponde
    

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        jsonReq = request.json
        sCodiceFiscale = jsonReq["codice fiscale"]
        anagrafe = JsonDeserialize(sAnagrafe)
        if sCodiceFiscale not in anagrafe:
            dNuovoCittadino = jsonReq
            anagrafe[sCodiceFiscale] = dNuovoCittadino
            JsonSerialize(anagrafe,sAnagrafe)
            jsonResp = {"Esito":"000", "Msg":"ok"}
            return json.dumps(jsonResp),200
        else:
            jsonResp = {"Esito":"001", "Msg":"Cittadino gia presente"}
            return json.dumps(jsonResp),200
    else:
        return 'Content-Type not supported!',401
    
@api.route('/read_cittadino', methods=['POST'])
def GestisciRichiestaCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        jsonReq = request.json
        sCodiceFiscale = jsonReq["codice fiscale"]
        anagrafe = JsonDeserialize(sAnagrafe)
        if sCodiceFiscale in anagrafe:
            jsonResp = {"Esito":"000", "Msg":anagrafe[sCodiceFiscale]}
            return json.dumps(jsonResp),200
        else:
            jsonResp = {"Esito":"001", "Msg":"Cittadino non presente"}
            return json.dumps(jsonResp),200
    else:
        return 'Content-Type not supported!',401

@api.route('/modifica_cittadino', methods=['POST'])
def GestisciModificaCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        jsonReq = request.json
        sCodiceFiscale = jsonReq["codice fiscale"]
        anagrafe = JsonDeserialize(sAnagrafe)
        if sCodiceFiscale in anagrafe:
            jsonResp = {"Esito":"000", "Msg":anagrafe[sCodiceFiscale]}
            return json.dumps(jsonResp),200
        else:
            jsonResp = {"Esito":"001", "Msg":"Cittadino non presente"}
            return json.dumps(jsonResp),200
    else:
        return 'Content-Type not supported!',401

@api.route('/elimina_cittadino', methods=['POST'])
def GestisciEliminaCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if content_type == 'application/json':
        jsonReq = request.json
        sCodiceFiscale = jsonReq["codice fiscale"]
        anagrafe = JsonDeserialize(sAnagrafe)
        if sCodiceFiscale in anagrafe:
            del anagrafe[sCodiceFiscale]
            JsonSerialize(anagrafe, sAnagrafe)
            jsonResp = {"Esito": "000", "Msg": "Cittadino eliminato con successo"}
            return json.dumps(jsonResp), 200
        else:
            jsonResp = {"Esito": "001", "Msg": "Cittadino non trovato"}
            return json.dumps(jsonResp), 200
    else:
        return 'Content-Type non supportato!', 401
    
#api.run(host="127.0.0.1", port=8080)
api.run(host="127.0.0.1", port=8080, ssl_context= 'adhoc')

