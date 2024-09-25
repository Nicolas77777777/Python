import json
# dato il file json quiz.json scrivere un programma che risponde alle seguenti domande:

#     quante domande ci sono nel questionario?
#     quante sono, in media, il numero di risposte possibili?
#     quante domande ci sono di matematica?


def Deserialize(file_path) -> dict:
    try:
        
        with open(file_path, "r") as json_file:
            
            dict_1 = json.load(json_file)
        
        return dict_1
    except Exception as errore:
     
        print(f" errore : {errore}")
        return None



dData= Deserialize("quiz.json")

def AnalisiDomande(dData:dict):
    totale_domande: int = 0 # 
    media_risposte: float = 0 
    for categoria, domande in dData["quiz"].items():
        for question, options in  domande.items():
            totale_domande += 1
            media_risposte = 
    print(f"quante domande ci sono nel questionario? {totale_domande}")

     

AnalisiDomande(dData)

# def printDeserialize(dData):
#     for key,values in dData.items():
#         print(key)
#         print (values)
#         print(len(key))
#         print(len(values))

#printDeserialize(Deserialize("quiz.json"))


# print()

