#QUESTION1
"""
"""
 
    
#QUESTION2
"""
"""
def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA == True or conditionB and conditionC == True:
        return "Operazione permessa"
    else:
        return "Operazione negata"

#QUESTION3
"""
Scrivi una funzione che prenda un dizionario e un valore,
e ritorni la prima chiave che corrisponde a quel valore,
o None se il valore non è presente.
"""

def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    for key, value in dizionario.items():
        if value == valore:
            return key


print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))
print(trova_chiave_per_valore({'k1': 'v1', 'k2': 'v2'}, 'v3'))
#QUESTION4
"""


"""
#QUESTION5
"""


"""
#QUESTION6
"""
Scrivi una funzione che unisce due dizionari. 
Se una chiave è presente in entrambi, somma i loro valori.
"""
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:

    d: dict = {}

    for key,value in dict1.items():
        if key in dict2:
            d[key] = value + dict2[key]
        else:
            d[key] = value
        
    for key,value in dict2.items():
        if key in dict1:
            d[key] = value + dict1[key]
        else:
            d[key] = value

    return d
                
print(merge_dictionaries({'x': 5}, {'x': -5})) #{'x': 0}
print(merge_dictionaries({}, {'a': 10, 'b': 20}))

#QUESTION7
"""
Scrivi una funzione che accetti tre parametri:
 username, password e status di attivazione dell'account
(attivo/non attivo). L'accesso è consentito solo 
se il nome utente è "admin", la password corrisponde 
a "12345" e l'account è attivo. 
La funzione ritorna "Accesso consentito" oppure "Accesso negato"

"""
def check_access(username: str, password: ..., is_active: bool) -> str:

    if is_active == True:
        if username == "admin" and password == "12345":
            return "Accesso consentito"
        
        elif username != "admin" and password == "12345":
            return "Accesso negato"
        
        elif username == "admin" and password != "12345":
            return "Accesso negato"
        
    elif is_active == False:
            return "Accesso negato"

        
print(check_access("admin", "12345", True))
print(check_access("admin", "12345", False))
print(check_access("user", "12345", True))
print(check_access("admin", "54321", True))
print(check_access("admin", "54321", False))

#QUESTION8
"""


"""
#QUESTION9
"""


"""
#QUESTION10
"""
Scrivere il frammento di codice che cambi 
il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato 
per 3 e gli deve essere sottratto 1."""

def transform(x: int) -> int:
    if x%2 == 0:
        return x//2
    elif x%2 != 0:
        return (x*3) -1


#QUESTION11
"""
Scrivi una funzione che prende una lista 
di numeri e ritorna un dizionario che classifica
i numeri in liste separate per numeri pari e dispari.
rint(classifica_numeri([1, 2, 3, 4, 5, 6])) """

	
def classifica_numeri(lista: int) -> dict[str:list[int]]:
    d:dict = dict()
    d["pari"]=[]
    d["dispari"]= []
    for i in lista:
        if i %2 == 0:
            d["pari"].append(i)
        elif i % 2 != 0:
            
            d["dispari"].append(i)

    return d 



print(classifica_numeri([1, 2, 3, 4, 5, 6]))



#QUESTION12
"""
Scrivi una funzione che, data una lista, ritorni un dictionary
che mappa ogni elemento alla sua frequenza nella lista.
"""
def frequency_dict(elements: list) -> dict:
    d:dict = {}
    for i in elements:
        if i not in d:
            d[i]= 1
        else:
            d[i] += 1

    return d

print(frequency_dict(['mela', 'banana', 'mela']))
print(frequency_dict(['a', 'b', 'c', 'a', 'b', 'c', 'a']))

#QUESTION13
"""
Scrivi una funzione che somma tutti i numeri
interi di una lista che sono maggiori 
di un dato valore intero definito threshold
"""

def sum_above_threshold(numbers: list[int], n:int) -> int:
    l:list =[]
    for i in numbers:
        if i > n:
            l.append(i)
            sum(l)
    return (l)

print(sum_above_threshold([15, 5, 25], 20))


#QUESTION14
"""
Scrivi una funzione che accetti un dizionario 
di prodotti con i prezzi e restituisca un nuovo
dizionario con solo i prodotti 
che hanno un prezzo superiore a 20, scontati del 10%
"""
def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    d:dict = dict()
    for key, value in prodotti.items(): 
        if value > 20:
            sconto= (value*10)/ 100
            d[key]= value -sconto
    return d


print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
#QUESTION15


"""
Scrivi una funzione che converta una
 lista di tuple (chiave, valore) in un dizionario. 
 Se la chiave è già presente, 
aggiungi il valore alla lista di
 valori già associata alla chiave.
 
"""
def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    d:dict = dict()

    for elements in tuples:
        if elements[0] not in d:
            d[elements[0]]= [elements[1]]
        else:
            d[elements[0]].append(elements[1])
    
    return d


print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)])) # {'a': [1, 3], 'b': [2]}