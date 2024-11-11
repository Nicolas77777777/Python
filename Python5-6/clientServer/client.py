import requests,json
import sys

base_url = "http://127.0.0.1:8080"


def GetDatiCittadino():
    nome = input("Qual'è il nome?")
    cognome = input("Qual'è il cognome")
    dataN = input("Qual'è la data di nascita?")
    codF = input("Qual'è il codice fiscale?")
  
    datiCittadino = {"nome":nome, "cognome": cognome, "data nascita":dataN, "codice fiscale":codF}
    return datiCittadino

def ReadCittadino():
    codF = input("Inserisci il codice fiscale")
    datiCittadino = {"codice fiscale":codF}
    return datiCittadino

def ModificaCittadino():

    codF = input("Inserisci il codice fiscale: ")
    campo_da_modificare = input("Quale dato vuoi modificare? (nome/cognome/data_nascita/codice_fiscale) ")
    nuovo_valore = input(f"Inserisci il nuovo valore per {campo_da_modificare}: ")

    datiCittadino = {
        "codice_fiscale": codF, 
        campo_da_modificare: nuovo_valore
    }
    return datiCittadino


def EliminaCittadino():
    
    codF = input("Inserisci il codice fiscale")

    datiCittadino = {"codice fiscale":codF}
    return datiCittadino

print("Operazioni disponibili:")
print("1. Inserisci cittadino (es. atto di nascita)")
print("2. Richiedi cittadino (es. cert. residenza)")
print("3. Modifica cittadino (es. cambio residenza)")
print("4. Elimina cittadino (es. trasferim altro comune)")
print("5. Esci")
sOper = input("Cosa vuoi fare?")
while(True):
    if sOper == "1":
        print("Richiesto atto di nascita")
        api_url = base_url + "/add_cittadino"
        jsonDataRequest = GetDatiCittadino()
        try:
            response = requests.post(api_url,json=jsonDataRequest)
        
            #print(response.json())
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)
        except:
            print("Problemi di comunicazione con il server, riprova più tardi")

    if sOper == "2":
        print("questo è il secondo ")
        print("Richiesto atto di nascita")
        api_url = base_url + "/read_cittadino"
        jsonDataRequest = ReadCittadino()
        try:
            response = requests.post(api_url, json=jsonDataRequest)
            print(f"Status Code: {response.status_code}")
            print(f"Risposta del server: {response.json()}")
        except:
            print("Problemi di comunicazione con il server, riprova più tardi.")
    
    if sOper == "3":
        print("questo è il terzo ")
        print("modifica dati cittadino")
        api_url = base_url + "'/modifica_cittadino'"
        jsonDataRequest = ModificaCittadino()
        try:
            response = requests.post(api_url, json=jsonDataRequest)
            print(f"Status Code: {response.status_code}")
            print(f"Risposta del server: {response.json()}")
        except:
            print("Problemi di comunicazione con il server, riprova più tardi.")

    if sOper == "4":
        print("questo è quarto ")
        print("elimina dati cittadino")
        api_url = base_url + "/elimina_cittadino"
        jsonDataRequest = EliminaCittadino()
        try:
            response = requests.post(api_url, json=jsonDataRequest)
            print(f"Status Code: {response.status_code}")
            print(f"Risposta del server: {response.json()}")
        except:
            print("Problemi di comunicazione con il server, riprova più tardi.")


    if sOper=="5":
        print("Buona giornata!")
        sys.exit()

    print("Operazioni disponibili:")
    print("1. Inserisci cittadino (es. atto di nascita)")
    print("2. Richiedi cittadino (es. cert. residenza)")
    print("3. Modifica cittadino (es. cambio residenza)")
    print("4. Elimina cittadino (es. trasferim altro comune)")
    print("5. Esci")
    sOper = input("Cosa vuoi fare?")

    