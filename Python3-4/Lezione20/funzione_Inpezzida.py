import math

def inPezzida(importo):
        
    banconote:list =[500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01] # creo lista 
    how_many_banconote: dict = {} # creo dizionario vuoto per inseire chiave banconote e valore la quantita utilizzata
    resti = {} # dizionario vuoto per il resto della divisione 
        
    #if isinstance(importo,int):  
    for banconota in banconote: # ciclo sulla lista banconote 
            
            how_many_banconote[banconota]=int(importo/banconota)
            resti[banconota] = math.fmod(importo,banconota)
            resto= math.fmod(importo,banconota)
            importo = resto
            print("quante banconote",how_many_banconote)

    for banconota, quantita in how_many_banconote.items():
            
            type : str = "banconota"
            types : str = "banconote"

            if banconota < 5:
                type : str = "moneta"
                types : str = "monete"
 
            if quantita  == 1 :
                print (f'{quantita} {type} da {banconota} euro') 
            elif quantita > 1:
                print (f'{quantita} {types} da {banconota} euro') 
                



    # elif isinstance(importo,float):
    #     print(False)


inPezzida(1024)
inPezzida(1023.88)
inPezzida(5353.94)











