import json
import jsonschema
import requests
import sys

# La funzione salva i dati in un file in formato JSON 
def JsonSerialize(data, sFile): # data: il file che vuoi salvare o i dati, s file il nome del file dove vuoi salvare le informazioni 
    with open(sFile, "w") as write_file: # Apre il file che hai scelto, "w" stiamo aprendo il file per scrivere (write)
        json.dump(data, write_file,indent=4)# Qui, prende i tuoi dati e li salva nel file, organizzandoli bene


# Legge i dati da un file (che è scritto in formato JSON) e li trasforma di nuovo
# in qualcosa che il computer può usare, come una lista o un dizionario.
def JsonDeserialize(sFile):
    with open(sFile, "r") as read_file:
        return json.load(read_file)


def print_list(lData,sRoot):
    for element in lData:
        if type(element) is str:
            print("\t" + element)
        #print(type(dData[keys]))
        if type(element) is dict:
            print_dictionary(element,sRoot)
        if type(element) is list:
            print_list(element,sRoot)



def print_dictionary(dData, sRoot):
    for keys, values in dData.items():
        if sRoot != "":
            print("Trovata chiave " + sRoot + "." + keys)
        else:
           print("Trovata chiave " + keys) 
        #print(values)
        #print(type(dData[keys]))
        if type(dData[keys]) is dict:
            if sRoot != "":
                print_dictionary(dData[keys],sRoot + "." + keys)
            else:
                print_dictionary(dData[keys],keys)
        if type(dData[keys]) is list:
            if sRoot != "":
                print_list(dData[keys],sRoot + "." + keys)
            else:
                print_list(dData[keys],keys)
    



