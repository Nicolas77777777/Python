

import requests, json, sys


base_url = "https://127.0.0.1:8080"

def Autenticazione():
    username = input("Inserisci username: ")
    password = input("Inserisci password: ")
    jsonDataRequest = {"username": username, "password": password}
    
    response = requests.post(base_url + "/Gestisci_Credenziali", json=jsonDataRequest, verify=False)
    if response.status_code == 200:
        dati = response.json()
        print(dati["Msg"])
        return dati["privilegio"]
    else:
        print("Errore di autenticazione")
        sys.exit()

privilegio = Autenticazione()


    


def GetDatiCittadino():
    nome = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    dataN = input("Inserisci la data di nascita (gg/mm/aaaa): ")
    codF = input("Inserisci il codice fiscale: ")
    datiCittadino = {
        "nome": nome, 
        "cognome": cognome, 
        "dataNascita": dataN, 
        "codFiscale": codF
    }
    return datiCittadino


def GetCodicefiscale():
    cod = input('Inserisci codice fiscale: ')
    return {"codFiscale": cod}

while True:
    print("\nOperazioni disponibili:")
    if privilegio == "write":
        print("1. Inserisci cittadino:") 
    else:
        print("1. Non autorizzato")
    print("2. Richiedi cittadino")
    if privilegio == "write":
        print("3. Modifica cittadino") 
    else:
        print("3. Non autorizzato")
    if privilegio == "write":   
        print("4. Elimina cittadino") 
    else:
        print("4. Non autorizzato")
    print("5. Esci")




    try:
        sOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue


    if sOper == 1:
        print("Aggiunta cittadino")
        api_url = base_url + "/add_cittadino"
        jsonDataRequest = GetDatiCittadino()
        response = requests.post(api_url, json=jsonDataRequest, verify = False)

    # Richiesta dati cittadino
    elif sOper == 2:
        print("Richiesta dati cittadino")
        api_url = base_url + "/read_cittadino"
        jsonDataRequest = GetCodicefiscale()
        response = requests.get(api_url + "/" + jsonDataRequest['codFiscale'], verify = False)
        print(response.json())

    elif sOper == 3:
        print("Modifica cittadino")
        api_url = base_url + "/update_cittadino"
        jsonDataRequest = GetDatiCittadino()
        response = requests.post(api_url, json=jsonDataRequest, verify = False)
        print(response.json())


    elif sOper == 4:
        print("Eliminazione cittadino")
        api_url = base_url + "/elimina_cittadino"
        jsonDataRequest = GetCodicefiscale()
        response = requests.post(api_url, json=jsonDataRequest, verify = False)
        print(response.json())


    elif sOper == 5:
        print("Buona giornata!")
        sys.exit()

    else:
        print("Operazione non disponibile, riprova.")


#