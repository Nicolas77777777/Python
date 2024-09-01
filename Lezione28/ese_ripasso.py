import math
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

    l=   []
    for key, value in dizionario.items():
        if value == valore:
            l.append(key)
    return l
        

print(trova_tutte_chiavi({'a': 1, 'b': 2, 'c': 1}, 1))
print(trova_tutte_chiavi({}, 1))

#QUESTION 3
def modifica_valore(n: int) -> int:
    """ 
    Scrivere un frammento di codice che modifichi il valore 
    intero memorizzato nella variabile n nel seguente modo:
    se n è pari, deve essere incrementato di 10;
    se n è dispari, deve essere decrementato di 5. """
    if n % 2 == 0:
       np= n+10
       return np
    else:
    
       nd= n -5
    return nd

n1 = 8
print(modifica_valore(n1))
#QUESTION 4 
#QUESTION 5

def calcola_stipendio(ore_lavorate: int) -> float:
    """
    Sviluppare una funzione in Python per calcolare lo stipendio 
    lordo di ciascuno dei diversi impiegati. L'azienda paga 10 
    dollari all'ora per le prime 40 ore di lavoro e paga "una volta
    e mezza" la paga oraria per tutte le ore di lavoro oltre le 40 ore.
 
    Per ogni operaio, viene fornito il numero di ore che tale impiegato
    ha lavorato durante la settimana.
    La vostra funzione deve ricevere questa informazione
    per ogni impiegato e determinare e stampare lo stipendio lordo."""

    if ore_lavorate <= 40:
        stipendio_lordo = ore_lavorate * 10 
        return stipendio_lordo
    else:
        ore_straordinarie= ore_lavorate -40
        ore_normali = ore_lavorate - ore_straordinarie
        p_ore_straordinarie= ore_straordinarie * 15
        p_ore_normali = ore_normali * 10
        stipendio_lordo = p_ore_normali + p_ore_straordinarie
        return stipendio_lordo
        
print(calcola_stipendio(40))
print(calcola_stipendio(0))
#QUESTION 6
#QUESTION 7
#QUESTION 8
def moltiplica_numeri(numbers: list[int], threshold: int) -> int:
    z: int=1
    for i in numbers:
        if i < threshold:
            z=z*i
    return z

print(moltiplica_numeri([15, 5, 25], 20))
#QUESTION 9
#QUESTION 10
#QUESTION 11
#QUESTION 12
#QUESTION 13
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    # cancella pass e scrivi il tuo codice
    pass
#QUESTION 14
#QUESTION 15
#QUESTION 16
def hypotenuse (x:float, y:float):
    """Definire una funzione chiamata hypotenuse 
    che calcoli la lunghezza dell'ipotenusa di un 
    triangolo rettangolo. La funzione deve ricevere 
    due argomenti di tipo float (corrispondenti ai due
    lati del triangolo) e restituire l'ipotenusa come un float.
    Per calcolare l'ipotenusa, si può ricorrere
    al teorema di Pitagora."""

    return math.sqrt(x**2 + y**2)

#QUESTION 17

