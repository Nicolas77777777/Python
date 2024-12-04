import requests,json
import sys

base_url = "https://127.0.0.1:8080"
auth = False

def AggiungiAutomobile():
    marca = input("Quale è  marca vuoi aggiungere? ")
    modello = input("Quale modello vuoi aggiungere? ")
    colore = input("In che colore? ")
    posizione = input("Dove vuoi locarla? ")
    filiale_id = input("Inserisci la filiale id: ")
    condizione = input("Qual'è lo stato della vettura? ")
    datiAutovettura = {"marca":marca, "modello": modello, "colore": colore, "posizione":posizione, "filiale_id":filiale_id, "condizione": condizione}
    return datiAutovettura

def GetAutomobile():
    marca = input("Qual'è la marca? ")
    modello = input("Qual'è il modello? ")
    colore = input("Qual'è il colore? ")
    condizione = input("Qual'è lo stato della vettura? ")
    datiAutomobile = {"marca":marca, "modello": modello, "colore": colore, "condizione": condizione}
    return datiAutomobile
    

def DeleteAutomobile():
    return input("Inserisci l'id della vettura venduta: ")



def AutoVenduta():
    data = input("Inserisci la data della vendita: ")
    id = input("Inserisci l'id dell'auto venduta: ")
    marca = input("Quale marca? ")
    modello = input("Quale modello? ")
    colore = input("Di che colore? ")
    condizione = input("Qual'è lo stato della vettura? ")
    autoVenduta = {data:{"id":id, "marca":marca, "modello": modello, "colore": colore, "condizione": condizione}}
    return autoVenduta



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
                print("Problemi  di comunicaz ione con il server, riprova più tardi")
        elif login == '2':
            api_url = base_url + '/registrazione'
            jsonDataRequest = Login()
            try:
                response = requests.post(api_url,json=jsonDataRequest, verify=False)
                print(response)
                print(response.content)
            except:
                print("Problemi di comunicazione con il server, riprova più tardi")
        elif login == '3':
            sys.exit()
        else:
            print("Errore operazione non esistente")
    else:        
        while(True):
            print("Operazioni disponibili:")
            print("1. Inserisci automobile ")
            print("2. Richiedi automobile ")
            #print("3. Modifica cittadino (es. cambio residenza)")
            print("3. Registra automobile venduta")
            print("4. Elimina automobile (es. venduta)")
            print("5. Logout")
            print("6. Esci")
            sOper = input("Cosa vuoi fare? ")
            if  sOper == "1":
                print("Inserisci automobile")
                api_url = base_url + "/add_automobile"
                jsonDataRequest = AggiungiAutomobile()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                    print(response.content)
                
                except:
                   print("Problemi di comunicazione con il server, riprova più tardi")
            elif  sOper == "2":
                print("Richiesta automobile")
                api_url = base_url + "/read_automobile"
                jsonDataRequest = GetAutomobile()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                    print(response.content)
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")    
                

            elif sOper == "3":
                print("Registra una  automobile venduta")
                api_url = base_url + "/vendita_automobile"
                jsonDataRequest = AutoVenduta()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                    print(response.content)
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")

           
            elif sOper == "4":
                print("Cancella automobile")
                api_url = base_url + "/delete_automobile"
                jsonDataRequest = DeleteAutomobile()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                    print(response.content)
                    
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")
            elif sOper == "5":
                auth = False
                print("Logout effetuato con successo")
                break
            elif sOper=="6":
                print("Buona giornata!")
                sys.exit()  
