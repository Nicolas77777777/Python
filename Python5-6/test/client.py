import requests,json
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://127.0.0.1:8080"
auth = False

def GetDatiAutomobile():
    # Richiesta dei dati per l'automobile
    marca = input("Qual è la marca dell'automobile? ") 
    modello = input("Qual è il modello dell'automobile? ")
    colore = input("Qual è il colore dell'automobile? ")
    targa = input("Qual è la targa dell'automobile? ")
    magazzino_id = input("Qual è l'ID del magazzino? ")
    condizione = input("Qual è la condizione dell'automobile (nuovo/usato)? ").lower()
    
    # Validazione del valore per la condizione
    if condizione not in ['nuovo', 'usato']:
        print("Errore: la condizione deve essere 'nuovo' o 'usato'. Impostazione predefinita su 'nuovo'.")
        condizione = 'nuovo'

    # Disponibilità predefinita a True
    disponibilita = True

    # Creazione del dizionario con i dati dell'automobile
    datiFindAutomobile = {
        "marca": marca,
        "modello": modello,
        "colore": colore,
        "targa": targa,
        "magazzino_id": int(magazzino_id),
        "condizione": condizione,
        "disponibilita": disponibilita
    }
    
    return datiFindAutomobile

def GetDatiMotocicletta():
    # Richiesta dei dati per l'automobile
    marca = input("Qual è la marca della Motocicletta? ") 
    modello = input("Qual è il modello della Motocicletta? ")
    colore = input("Qual è il colore della Motocicletta? ")
    targa = input("Qual è la targa della Motocicletta? ")
    magazzino_id = input("Qual è l'ID del magazzino? ")
    condizione = input("Qual è la condizione della Motocicletta (nuovo/usato)? ").lower()
    
    # Validazione del valore per la condizione
    if condizione not in ['nuovo', 'usato']:
        print("Errore: la condizione deve essere 'nuovo' o 'usato'. Impostazione predefinita su 'nuovo'.")
        condizione = 'nuovo'

    # Disponibilità predefinita a True
    disponibilita = True

    # Creazione del dizionario con i dati dell'automobile
    datiFindMotocicletta = {
        "marca": marca,
        "modello": modello,
        "colore": colore,
        "targa": targa,
        "magazzino_id": int(magazzino_id),
        "condizione": condizione,
        "disponibilita": disponibilita
    }
    
    return datiFindMotocicletta

def CercaAutomobile():
    # Chiedi all'utente i criteri di ricerca
    marca = input("Inserisci la marca dell'automobile (opzionale): ")
    modello = input("Inserisci il modello dell'automobile (opzionale): ")
    colore = input("Inserisci il colore dell'automobile (opzionale): ")
    condizione = input("Inserisci la condizione (nuovo/usato, opzionale): ")

    # Creazione del dizionario dei criteri
    criteri = {}
    if marca:
        criteri['marca'] = marca
    if modello:
        criteri['modello'] = modello
    if colore:
        criteri['colore'] = colore
    if condizione:
        criteri['condizione'] = condizione

    data = {"criteri": criteri}

    try:
        # risposta = richiesta
        response = requests.post(f"{base_url}/cerca_automobile", json=data, verify=False)
        if response.status_code == 200:
            data = response.json()['data']
            print("Automobili trovate:")
            for auto in data:
                print(
                    f"ID: {auto['id']}, Marca: {auto['marca']}, Modello: {auto['modello']}, "
                    f"Colore: {auto['colore']}, Condizione: {auto['condizione']}, Disponibilità: {auto['disponibilita']}, "
                    f"Filiale: {auto['filiale_nome']} ({auto['filiale_indirizzo']})"
                )
        elif response.status_code == 404:
            print(response.json().get('message', 'Nessuna automobile trovata'))
        else:
            print(f"Errore: {response.json().get('message', 'Errore nella ricerca')}")
    except Exception as e:
        print(f"Errore di connessione: {e}")


def UpdateCittadino():
    dati_da_modifcare = [None for _ in range(4)]
    dati_da_modifcare[0] = input("Inserisci il codice fiscale della persona a cui vuoi modificarei i dati: ")
    nome = input("Inserisci il nome modificato (Lascia vuoto per non cambiare): ")
    cognome = input("Inserisci il cognome modificato (Lascia vuoto per non cambiare): ")
    dataN = input("Inserisci la data di nascita modificata (Lascia vuoto per non cambiare): ")
    if cognome:
        dati_da_modifcare[1] = cognome
    if dataN:
        dati_da_modifcare[2] = dataN
    if nome:
        dati_da_modifcare[3] = nome
    return dati_da_modifcare

def DeleteCittadino():
    return input("Inserisci il codice fiscale della persona da eliminare: ")

def Login():
    username = input("Inserisci l'username: ")
    password = input("Inserisci la password: ")
    return {username: [password]}

stato = -1

while True:
    if not auth:
        print("Operazioni disponibili:")
        print("1. Login")
        print("2. Cerca Automobile")
        print("3. Esci")
        login = input("Cosa vuoi fare? ")

        if login == '1':
            api_url = base_url + '/login'
            accesso = Login()
            try:
                response = requests.post(api_url,json=accesso, verify=False)
                print(response.content)
                jResponse = response.json()
                if jResponse['Esito'] == "ok":
                    auth = True
                    stato = jResponse['Stato']
                print(auth)
            except:
                print("Impossibile ")
    

        elif login =='2':
            print("Cerca Automobile")
            api_url = base_url + "/cerca_automobile"
            jsonDataRequest = CercaAutomobile()

            try:
                response = requests.post(api_url,json=jsonDataRequest, verify=False)
                print("auto trovata con sucesso")
                    
            except:
                print("Impossibile trovare l'auto")
    
        elif login == '3':
            sys.exit()
        else:
            print("Errore operazione non esistente")
    else:        
        while(True):
            print("Operazioni disponibili:")
            print("1. Inserisci Automobile")
            print("2. Inserisci Motocicletta ")
            print("3. Registra nuovo admin")
            print("4. Vendite Giornaliere")
            print("5. Logout")
            print("6. Esci")
            sOper = input("Cosa vuoi fare? ")
            if sOper == "1":
             
                print("Inserisci Automobile")
                api_url = base_url + "/add_automobile"

                jsonDataRequest = GetDatiAutomobile()

                try:
                     # Debug: Stampare i dati inviati
                    print(f"Dati inviati: {jsonDataRequest}")
                    
                    response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                    print(response.content)
                
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")

            elif sOper == "2":
                api_url = base_url + "/add_motocicletta"

                jsonDataRequest = GetDatiMotocicletta()

                try:
                     # Debug: Stampare i dati inviati
                    print(f"Dati inviati: {jsonDataRequest}")
                    
                    response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                    print(response.content)
                
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")

            elif sOper == "3":
                api_url = base_url + '/registrazione'
                jsonDataRequest = Login()
                
                try:
                    response = requests.post(api_url,json=jsonDataRequest, verify=False)
                    print(response)
               
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")

            elif sOper == "3":
                pass
                    
            elif sOper == "5":
                auth = False
                print("Logout effetuato con successo")
                break
            elif sOper=="6":
                print("Buona giornata!")
                sys.exit()  
