import requests,json
import sys

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
    # Richiesta dei dati per l'automobile
    marca = input("Qual è la marca dell'automobile? ") 
    modello = input("Qual è il modello dell'automobile? ")
    colore = input("Qual è il colore dell'automobile? ")
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
        "condizione": condizione,
        "disponibilita": disponibilita
    }
    
    return datiFindAutomobile
    #return input("Inserisci il codice fiscale della persona richiesta: ")
    pass
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
        print("2. Registrazione")
        print("3. Cerca Automobile")
        print("4. Esci")
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
                print("Problemi di comunicazione con il server, riprova più tardi")
        elif login == '2':
            api_url = base_url + '/registrazione'
            jsonDataRequest = Login()
            try:
                response = requests.post(api_url,json=jsonDataRequest, verify=False)
                print(response)
                print(response.content)
            except:
                print("Problemi di comunicazione con il server, riprova più tardi")

        elif login =='3':
            print("Cerca Automobile")
            api_url = base_url + "/cerca_automobile"
            jsonDataRequest = CercaAutomobile()
            try:
                response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                print(response.content)
                    
            except:
                print("Problemi di comunicazione con il server, riprova più tardi")
    
        elif login == '4':
            sys.exit()
        else:
            print("Errore operazione non esistente")
    else:        
        while(True):
            print("Operazioni disponibili:")
            print("1. Inserisci Automobile")
            print("2. Inserisci Motocicletta ")
            print("3. Elimina cittadino (es. trasferim altro comune)")
            print("4. Logout")
            print("5. Esci")
            sOper = input("Cosa vuoi fare? ")
            if sOper == "1":
             
                print("Inserisci Automobile")
                #api_url = base_url + "/add_cittadino"
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
                print("Richiesto cittadino")
                api_url = base_url + "/delete_cittadino"
                jsonDataRequest = DeleteCittadino()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                    print(response.content)    
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")
            elif sOper == "4":
                auth = False
                print("Logout effetuato con successo")
                break
            elif sOper=="5":
                print("Buona giornata!")
                sys.exit()  
