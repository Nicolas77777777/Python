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
            
            if quantita != 0 and quantita <= 1 :
                print (f'{quantita} Banconota da {banconota} euro') 
            elif quantita > 1:
                print (f'{quantita} Banconote da {banconota} euro') 
            elif quantita != 0 and quantita <= 1 and  banconota == 2 or  1 or 0.5 or 0.2 or 0.1 or  0.05 or 0.02 or 0.01:
                
                    print (f'{quantita} monete da {banconote} euro')



    # elif isinstance(importo,float):
    #     print(False)


inPezzida(1024)









