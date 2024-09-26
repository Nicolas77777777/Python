import json
"""dato il file json quiz.json scrivere un programma che risponde alle seguenti domande:

    quante domande ci sono nel questionario?
    quante sono, in media, il numero di risposte possibili?
    quante domande ci sono di matematica?"""

def Deserialize(file_path) -> dict:
    try:
        
        with open(file_path, "r") as json_file:
            
            dict_1 = json.load(json_file)
        
        return dict_1
    except Exception as errore:
     
        print(f" errore : {errore}")
        return None
    

def AnalisiDomande(dData:dict) -> str:
    totaleDomande: int = 0 
    totaleRisposte: float = 0 
    totaleDomandeMatematica: int = 0
    for categoria, q in dData["quiz"].items():
        #print(categoria)
        for question, values in  q.items():
            # print(question)
            # print(values)
            totaleDomande += 1
            totaleRisposte += len(values["options"])
            
    mediaRisposte =totaleRisposte/totaleDomande
        
            # for question, options in values.items():
            #     print(question)
            #     print(options)
            #     mediaRisposte =len(options["options"])

    for qMath, values in dData["quiz"]["maths"].items():
        print(qMath)
        totaleDomandeMatematica += 1

    return (
        f"Quante domande ci sono nel questionario? {totaleDomande}\n"
        f"Quante sono, in media, il numero di risposte possibili? {mediaRisposte:.2f}\n"
        f"Quante domande ci sono di matematica? {totaleDomandeMatematica}"
    )


   
dData= Deserialize("quiz.json")
print(AnalisiDomande(dData))


