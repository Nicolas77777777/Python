import requests,json
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://127.0.0.1:8080"
auth = False

def GetDatiImmobileAffitto():
   
    try:
        # Richiesta dei dati per immobile
        catastale = input("Inserisci il codice catastale dell'immobile: ")
        indirizzo = input("Qual è l'indirizzo dell'immobile? ")
        numero_civico = int(input("Qual è il numero civico dell'immobile? "))
        tipo_affitto = input("Qual è il tipo di affitto (PARZIALE/TOTALE): ").strip().upper()
        bagno_personale = input("L'immobile ha un bagno personale? (Sì/No): ").strip().lower() == 'sì'
        prezzo_mensile = int(input("Qual è il prezzo mensile dell'immobile? "))
        filiale_proponente = input("Qual è la partita IVA della filiale proponente? ")

        # Validazione del tipo di affitto
        if tipo_affitto not in ["PARZIALE", "TOTALE"]:
            print("Tipo di affitto non valido. Impostato a 'PARZIALE'.")
            tipo_affitto = "PARZIALE"

        # Creazione del dizionario con i dati dell'immobile
        immobile = {
            "catastale": catastale,
            "indirizzo": indirizzo,
            "civico": numero_civico,
            "tipo_affitto": tipo_affitto,
            "bagno_personale": bagno_personale,
            "prezzo_mensile": prezzo_mensile,
            "filiale_proponente": filiale_proponente,
        }

        print("Dati raccolti con successo.")
        return immobile

    except ValueError as ve:
        print(f"Errore nei dati numerici: {ve}. Riprova.")
        return None
    except Exception as e:
        print(f"Errore inaspettato: {e}.")
        return None

    

def GetDatiImmobileVendita():
    # Richiesta dei dati per immobile
    # Raccolta dati dall'utente
        catastale = input("Inserisci il codice catastale dell'immobile: ")
        indirizzo = input("Qual è l'indirizzo dell'immobile? ")
        numero_civico = int(input("Qual è il numero civico dell'immobile? "))
        piano = input("Qual è il piano dell'immobile? (Lascia vuoto se non applicabile): ")
        metri = int(input("Quanti metri quadrati ha l'immobile? "))
        vani = int(input("Quanti vani ha l'immobile? "))
        prezzo = int(input("Qual è il prezzo di vendita dell'immobile? "))
        stato = input("Qual è lo stato dell'immobile (LIBERO/OCCUPATO)? ").strip().upper()
        filiale_proponente = input("Qual è la partita IVA della filiale proponente? ")

     # Validazione dello stato
        if stato not in ["LIBERO", "OCCUPATO"]:
            print("Stato non valido. Impostato a 'LIBERO'.")
            stato = "LIBERO"

    

    # Creazione del dizionario con i dati dell'automobile
        immobile = {
            "catastale": catastale,
            "indirizzo": indirizzo,
            "numero_civico": numero_civico,
            "piano": int(piano) if piano else None,
            "metri": metri,
            "vani": vani,
            "prezzo": prezzo,
            "stato": stato,
            "filiale_proponente": filiale_proponente,
        }

        print("Dati raccolti con successo.")
        return immobile

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
            print("1. Aggingi Immobile per L'affitto")
            print("2. Aggiungi immobile per la vendita ")
            print("3. Registra nuovo admin")
            print("4. Vendite Giornaliere")
            print("5. Logout")
            print("6. Esci")
            sOper = input("Cosa vuoi fare? ")

            if sOper == "1":
             
                print("Inserisci Immobile per l'affitto")
                api_url = base_url + "/add_immobile_affitto"

                jsonDataRequest = GetDatiImmobileAffitto()

                try:
                     # Debug: Stampare i dati inviati
                    print(f"Dati inviati: {jsonDataRequest}")
                    
                    response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                    print(response.content)
                
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")

            elif sOper == "2":
                api_url = base_url + "/add_immobile_vendita"

                jsonDataRequest = GetDatiImmobileVendita()

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

            elif sOper == "4":
                pass
                    
            elif sOper == "5":
                auth = False
                print("Logout effetuato con successo")
                break
            elif sOper=="6":
                print("Buona giornata!")
                sys.exit()  
