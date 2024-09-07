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
def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    """Scrivi una funzione che accetti un dizionario di prodotti 
    con i relativi prezzi e restituisca un nuovo dizionario con 
    solo i prodotti che hanno un prezzo inferiore a 50, 
    ma con i prezzi aumentati del 10% e 
    arrotondati a due cifre decimali."""

    newdiz:dict= {}
    for key,value in prodotti.items():
        if  value < 50.0:
            new_price =  round(value* 1.10,2)
            newdiz[key] = new_price
    return newdiz

print(filtra_e_mappa({"prodotto1": 30.0, "prodotto2": 60.0, "prodotto3": 45.0})) #{'prodotto1': 33.0, 'prodotto3': 49.5}
print(filtra_e_mappa({"prodotto1": 55.0, "prodotto2": 70.0, "prodotto3": 80.0}))

	


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
    """Scrivi una funzione che unisce due dizionari. 
    Se una chiave è presente in entrambi, 
    moltiplica i loro valori."""
    dict3 ={}
    for key, value in dict1.items():
        if key in dict2:
            dict3[key] = value * dict2[key]
        else:
            dict3[key] = value
    for key, value in dict2.items():
        if key in dict1:
            dict3[key] = value * dict1[key]
        else:
            dict3[key] = value
    return dict3

        

print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
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
def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    """Scrivi una funzione che converta una lista 
    di tuple (chiave, valore) in un dizionario. 
    Se la chiave è già presente, somma il valore
    al valore già associato alla chiave."""

    dict1 = {}
    for chiave, valore in tuples:
        if chiave not in dict1:
            dict1[chiave] = valore
        else:
            dict1[chiave] += valore
    return dict1


print(lista_a_dizionario([("a", 1), ("b", 2), ("c", 3)])) # risultato{'a': 1, 'b': 2, 'c': 3}
print(lista_a_dizionario([("a", 1), ("a", 2), ("a", 3)]))

	

#QUESTION 18
def classifica_numeri(lista: int) -> dict[str:list[int]]:
    """Scrivi una funzione che prenda una lista
    di numeri e ritorni un dizionario che classifichi
    i numeri in liste separate per numeri positivi e negativi."""

    diz: dict={}
    diz["positivi"]=[]
    diz["negativi"]=[]

    for ele in lista:
        if ele < 0:
            diz["negativi"].append(ele)
        else:
            diz["positivi"].append(ele)
    return diz

print(classifica_numeri([1, -2, 3, -4, 5, -6, 7, -8, 9, -10]))
