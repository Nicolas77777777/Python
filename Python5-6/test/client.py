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

def CercaImmobileVendita():
    try:
        # Chiedi all'utente i criteri di ricerca
        piano = input("Qual è il piano dell'immobile? (Lascia vuoto se non applicabile): ")
        metri = input("Quanti metri quadrati ha l'immobile? (Lascia vuoto per non specificare): ")
        vani = input("Quanti vani ha l'immobile? (Lascia vuoto per non specificare): ")
        prezzo = input("Qual è il prezzo massimo dell'immobile? (Lascia vuoto per non specificare): ")
        stato = input("Qual è lo stato dell'immobile (LIBERO/OCCUPATO)? (Lascia vuoto per non specificare): ").strip().upper()

        # Creazione del dizionario dei criteri
        criteri = {}
        if piano:
            criteri['piano'] = int(piano)
        if metri:
            criteri['metri'] = int(metri)
        if vani:
            criteri['vani'] = int(vani)
        if prezzo:
            criteri['prezzo'] = int(prezzo)
        if stato:
            if stato not in ["LIBERO", "OCCUPATO"]:
                print("Stato non valido. Ignorato.")
            else:
                criteri['stato'] = stato

        # Creazione del payload per la richiesta
        data = {"criteri": criteri}

        # Invio della richiesta al server
        response = requests.post(f"{base_url}/cerca_immobile_vendita", json=data, verify=False)

        # Gestione della risposta
        if response.status_code == 200:
            risultati = response.json().get('data', [])
            if risultati:
                print("Immobili trovati:")
                for immobile in risultati:
                    print(
                        f"Codice catastale: {immobile['catastale']}, Indirizzo: {immobile['indirizzo']}, "
                        f"Numero Civico: {immobile['numero_civico']}, Piano: {immobile.get('piano', 'N/A')}, "
                        f"Metri: {immobile['metri']}, Vani: {immobile['vani']}, "
                        f"Prezzo: {immobile['prezzo']}, Stato: {immobile['stato']}, "
                        f"Filiale proponente: {immobile['filiale_proponente']}"
                    )
            else:
                print("Nessun immobile trovato con i criteri specificati.")
        elif response.status_code == 404:
            print(response.json().get('message', 'Nessun immobile trovato'))
        else:
            print(f"Errore: {response.json().get('message', 'Errore nella ricerca')}")

    except ValueError:
        print("Errore nei dati inseriti: assicurati di inserire numeri validi per i campi numerici.")
    except Exception as e:
        print(f"Errore di connessione: {e}")


def Login():
    username = input("Inserisci l'username: ")
    password = input("Inserisci la password: ")
    return {username: [password]}

stato = -1

while True:
    if not auth:
        print("Operazioni disponibili:")
        print("1. Login")
        print("2. Cerca Immobile in Vendita")
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
            print("Cerca Immobile in Vendita")
            api_url = base_url + "/cerca_immobile_vendita"
            jsonDataRequest = CercaImmobileVendita()

            try:
                response = requests.post(api_url,json=jsonDataRequest, verify=False)
                print("Immobile  trovato con sucesso")
                    
            except:
                print("Impossibile trovare l'immobile")
    
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
