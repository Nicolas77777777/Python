#QUESTION 1
def mappa_parole_a_lunghezza(words: list) -> dict:
    # cancella pass e scrivi il tuo codice
    newdict={}
    for i in words:
        newdict[i]= len(i)
    return newdict
    
print(mappa_parole_a_lunghezza(["apple", "banana", "cherry"]))

#QUESTION 2
def trova_tutte_chiavi(dizionario: dict[str: int], valore: int) -> str:
    """
    Scrivi una funzione che prenda un dizionario e un valore, 
    e ritorni una lista con tutte le chiavi che corrispondono
    a quel valore, o una lista vuota se il valore non è presente.
    """
    for key, value in dizionario.items():
        if key == valore:

            x= list(key)
    return x
        
    


        

print(trova_tutte_chiavi({'a': 1, 'b': 2, 'c': 1}, 1))
print(trova_tutte_chiavi({}, 1))

	



#QUESTION 3
#QUESTION 4 
#QUESTION 5
#QUESTION 6
#QUESTION 7
#QUESTION 8
#QUESTION 9
#QUESTION 10
#QUESTION 11
#QUESTION 12
#QUESTION 13
#QUESTION 14
#QUESTION 15
#QUESTION 16
#QUESTION 17

