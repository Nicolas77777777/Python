import random
from collections import defaultdict
from driver import create_list


# 1Scrivi una funzione che prenda un dizionario e un valore, 
# e ritorni la prima chiave che corrisponde a quel valore, 
# o None se il valore non è presente.

def cerca_valore_diz (diz: dict, valore):

        for key, value in diz.items():
            if value == valore:
                print (key)
                return key 
        else:
                print(None)
        

dit: dict = {"a":1,"b":2}

cerca_valore_diz(dit,2)
    
# 2. Scrivi una funzione che inverte le chiavi e i valori in un dizionario.
# Se ci sono valori duplicati, scarta i duplicati.

def inverte_valori_dizionario( diz: dict ) -> dict:
    diz_inverso: dict = {}

    for key, value in diz.items():
            diz_inverso[value]= key

            return diz_inverso
    
print (f'{inverte_valori_dizionario(dit)}\n')
      
     
# 3Scrivi una funzione che riceve una lista di numeri,
#  filtra i numeri pari, e restituisce una nuova 
#  lista con i numeri pari moltiplicati per un fattore dato

def lista_numeri_pari_per_fattore (l1: list[int], fattore: int) -> list:
    l2=[] # liste vuote
    l3= [] # liste vuote
    for elemento in l1 : # per ogni elemento in lista 
        if elemento % 2 == 0: # se l'elemento è divisibile per 2 con resto ugale a 0 PARI
            l2.append(elemento) # aggiungi alla lista gli elementi 

    for i in l2: # cicla eleemnti della lista nuova creata con numeripari 
        l3.append(i*fattore) # aggiungi alla lista l3 tutti gli elementi della lista e moltiplicali per il fatootre 
    
    return l2,l3
          
l1 = [] # creo una lista vuota
for i in range(10): # con una linghezza massima di 10 elementi 
    l1.append(random.randint(0,1000)) # aggingi gli elementi random di numeri tra 0 e 1000

print (f'{l1} {len(l1)}\n')
l5= [7,3,4,5,6,8,10]

print(f'{lista_numeri_pari_per_fattore(l1,2)}\n')

 
# 4Scrivi una funzione che determina se un numero è 'magico'. 
# Un numero è considerato magico se è 
# divisibile per 4 ma non per 6.

def magic_number (num: int ) -> str : 
    if num % 4 == 0 and  num % 6 != 0 :
        return f'{num} is a magic number'
     
    else:
        return f'{num} is not a magic number'
    
print(f'{magic_number(66)}')

print(f'{magic_number(60)}')

print(f'{magic_number(8)}\n')


# 5Scrivi una funzione che accetti una lista di numeri
# e ritorni la somma dei numeri che 
# sono divisibili sia per 2 che per 3.

def sum_num (l1: list) -> int:

    lsum = []
    for elemento in l1:
        if elemento % 2 == 0 and elemento % 3 == 0:
            lsum.append(elemento)
        
    return (sum(lsum))

l3=[3,3,4,5,6,7,8,9,10,12,16,18]
l4=[6,16,18]

print(sum_num(l1))

print(sum_num(l3))

print(sum_num(l4))


#6 Scrivi una funzione che accetti un dizionario
# di prodotti con i prezzi e restituisca un nuovo dizionario 
# con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.

def prodotti_sup_20 (diz: dict):
    new_dict: dict= {}
    for key, value in diz.items():
            if value > 20:
                sconto =(value * 10 /100)
                new_dict[key] = value - sconto 
            
 
    return sconto,diz,new_dict
 

store: dict = dict(Maglietta= 18, Jeans = 25, calze= 6, Felpa= 30)

print(prodotti_sup_20(store))

# 7. Scrivi una funzione che prenda in input 
# una lista di dizionari che rappresentano voti 
# di studenti e aggrega i voti per studente 
# in un nuovo dizionario.

def aggrega_voti (li:list) -> dict:
    voti={}
    for i in li:
        studente =i['nome']
        voto = i['voto']
        if studente in voti:
            voti[studente].append(voto)
        else:
            voti[studente]=[voto]
    return voti

# lista_voti = [
#      {'studente': 'Franca','voto':30},
#      {'studente': 'Gino','voto':30},
#      {'studente': 'Sonia','voto':30},
#      {'studente': 'Dario','voto':18},
#      {'studente': 'Sonia','voto':29},
#      {'studente': 'Simone','voto':27},
#      {'studente': 'Dario','voto':20}   ]


print(aggrega_voti([{'nome': 'Alice', 'voto': 90},
                    {'nome': 'Bob', 'voto': 75},
                    {'nome': 'Alice', 'voto': 85}]))

 
"""Scrivi una funzione che elimini dalla lista 
dati certi elementi specificati in un dizionario. 
Il dizionario contiene elementi da rimuovere 
come chiavi e il numero di volte che devono essere rimossi come valori."""
 
# 9. Scrivi una funzione che converta una lista di
# tuple (chiave, valore) in un dizionario.
# Se la chiave è già presente, aggiungi 
# il valore alla lista di valori già associata alla chiave."""

def roscio (l1:list) -> dict:
    newdict: dict = {}
    for elements in l1:
        if elements[0] in newdict:
             newdict[elements[0]].append(elements[1])
        else:
             newdict[elements[0]]=[elements[1]]
             
    return newdict
####### altro metodo 
def elimina_duplicati(l1:list)-> dict:
    newdict: dict = {}

    for elemento in l1: 
        if elemento[0] not in newdict:
            newdict[elemento[0][0]]=[]
            newdict[elemento[0]].append(elemento[1])
        else: 
            newdict[elemento[0]].append(elemento[1])

    return newdict


# d = defaultdict(list)
# for k in t:
#     d[k[0]].append(k[1])
     
thistuplelist = [ ("a", 1), ("b",2), ("c",3), ("a",4), ("b", 6)]

print(roscio(thistuplelist))
print(elimina_duplicati(thistuplelist))

 
# 10. Scrivi una funzione che prende una lista
#  di numeri e ritorna un dizionario che classifica 
#  i numeri in liste separate per numeri pari e dispari.

def dizPariDispari(l1:list) -> dict:
    diz_num_pari_dispari: dict = {}
    diz_num_pari_dispari["Pari"] = []
    diz_num_pari_dispari["Dispari"]= []
    for i in l1:
        if i %2== 0:
            diz_num_pari_dispari['Pari'].append(i)
        else:    
            diz_num_pari_dispari['Dispari'].append(i)

    return diz_num_pari_dispari

l7=[]
for i in range(20):
    x= random.randint(0,100)
    l7.append(x)

print(l7)

print(dizPariDispari(l7))

# 11. Scrivi una funzione che converte una 
# temperatura da gradi Celsius a Fahrenheit 
# e viceversa a seconda del parametro. 
# Utilizza il concetto di parametri opzionali.

def convert_temperature(temperature: float, to_fahrenheit: bool = True) -> float:
    """
    Converte la temperatura tra gradi Celsius e Fahrenheit.
    
    :param temperature: La temperatura da convertire.
    :param to_fahrenheit: Se True, converte da Celsius a Fahrenheit. 
                          Se False, converte da Fahrenheit a Celsius.
    :return: La temperatura convertita.
    """
    if to_fahrenheit:
        # Conversione da Celsius a Fahrenheit
        return (temperature * 9/5) + 32
    else:
        # Conversione da Fahrenheit a Celsius
        return (temperature - 32) * 5/9

# Esempi di utilizzo della funzione
print(f"25°C -> {convert_temperature(25, to_fahrenheit=True)}°F")
print(f"77°F -> {convert_temperature(77, to_fahrenheit=False)}°C")

 
""" Scrivi una funzione che somma tutti i numeri
interi di una lista che sono maggiori di un 
dato valore intero definito threshold."""
 
def threshold(l1:int, fattore: int):
    newlist=[]
    for i in l1:
        if i > fattore:
            newlist.append(i)
    return sum(newlist)

l10=[1,1,1,2,3,3,3,]
l8=[2,3,4,5,6,7,8,9]
print(threshold(l8, 4))
print(threshold(l10, 2))


# 13. Scrivi una funzione che, data una lista, 
# ritorni un dictionary che mappa ogni 
# elemento alla sua frequenza nella lista.

def frequency_dict (l1:list) -> dict:
    diz = {}
    for item in l1:
        if item in diz:
            diz[item] += 1
        else:
            diz[item] = 1
    return diz


print(frequency_dict(['mela', 'banana', 'mela','pera', 'mela', 'banana']))
# {'mela': 2, 'banana': 1}
	


# """14. Scrivi una funzione che ritorna un
#  dizionario che unisce due dizionari. 
#  Se una chiave è presente in entrambi, 
#  somma i loro valori nel nuovo dizionario."""

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
        newdict: dict ={}
        x=dict2.values
        for key, value in dict1.items():
            if key in dict2:
                newdict[key]= value + dict2[key]
            else :
                newdict[key]= value
        for key, value in dict2.items():
            if key in dict1:
                newdict[key]= value + dict1[key]
            else :
                newdict[key]= value
        return newdict
        

    
print(merge_dictionaries({'x': 5}, {'x': -5}))

 
# 15. Scrivi una funzione che, dato un insieme
#  e una lista di numeri interi da rimuovere,
# ritorni un nuovo insieme senza i numeri
# specificati nella lista.

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    new_set = original_set.copy()
    list_set= list(new_set)
    for elements in elements_to_remove:
        if elements in new_set:
            new_set.remove(elements)
    return new_set
 
# 16. Scrivi una funzione che ritorna il valore
#  massimo, minimo e la media di
#  una lista di numeri interi.

def min_max_mid(l1:list):
    mass= max(l1)
    minim= min(l1)
    somma = sum(l1)
    med = sum(l1)/ len(l1)

    return mass,minim, med, somma


l11: list =[]
for i in range(10):
    z= random.randint(0,10)
    l11.append(z)

print (l11)

print(min_max_mid(l11))

# 17. Scrivi una funzione che calcola la media 
# di una lista di numeri e ritorna il valore 
# arrotondato all'intero più vicino.

def mid (l1:list):
    
    len1= len(l1)
    sum1= sum(l1)
    avg = sum(l1)/ len(l1)
    roundavg = round(avg)

    return roundavg, avg, sum1, len1

l12=[1,2,3,4,5,6,6,67,7,8,8,9]          
print(mid(l12))

"""18. Scrivi una funzione che rimuove tutti 
i duplicati da una lista, contenente sia numeri che 
lettere, mantenendo l'ordine originale degli elementi."""
 
# 19. Scrivi una funzione che ruota gli elementi di
#  una lista verso sinistra di un numero specificato
# k di posizioni. La rotazione verso sinistra significa
# che ciascun elemento della lista viene spostato a sinistra 
# di una posizione e l'elemento iniziale viene spostato alla
# fine della lista. Per la rotazione utilizzare lo slicing
# e gestire il caso in cui il numero specificato di posizioni 
# sia maggiore della lunghezza della lista.

def rotatesx (l1: list, k: int ) -> list:

    if k >= len(l1):
        
        k1 = k % len(l1)

        return l1[k1:] + l1[:k1]
    
    else :

        return l1[k:] + l1[:k]
        

l12: list =[1,2,3,4,5,6,7,8,9,10]

print(rotatesx(l12,2))
print(rotatesx(l12,3))
print(rotatesx(l12,4))
print(rotatesx(l12,5))


    
"""20. Scrivi una funzione che accetti tre parametri: username,
 password e status di attivazione dell'account 
 (attivo/non attivo). L'accesso è consentito
solo se il nome utente è "admin", 
la password corrisponde a "12345" e l'account è attivo."""

def account(username: str, password: float, stato_attivazione= None):

    if username == "admin" and password == "12345":
        stato_attivazione = True
        return stato_attivazione
    else:
        stato_attivazione = False
        return stato_attivazione

print(account("admin","12345")) 
print(account("adin","1234")) 


""""21. Scrivi una funzione che verifica 
se una combinazione di condizioni (A, B, e C) 
è soddisfatta per procedere con un'operazione.
 L'operazione può procedere solo se la condizione
A è vera o se entrambe le condizioni B e C sono vere."""

def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA == True or conditionB and conditionC == True:
        return "operazione permessa"
    else:
        return "operazione non permessa"
 
"""22. Scrivi una funzione che riceve un numero
 e stampa un conto alla rovescia da quel numero a zero."""

def num_rovescio(num: int ):
    for i in range(num +1):
        num-1
        print (i)

num_rovescio(20)

def conto_alla_rovescia(n:int ):
    # Controlla se il numero è non negativo
    if n < 0:
        print("Per favore, inserisci un numero non negativo.")
        return
    
    # Esegue il conto alla rovescia
    while n >= 0:
        print(n)
        n -= 1


numero = 10
conto_alla_rovescia(numero)


"""23. Scrivi una funzione che, dato un numero intero, 
determina se è un "numero magico". 
Un numero magico è definito come un 
numero che contiene il numero 7."""

def is_magic_number(num: int) -> bool:
    num_str= str(num)

    for element in num_str:
        if "7" in num_str:
            return True
        
        else: 
            return False
        
print(is_magic_number(7))

print(is_magic_number(70))
print(is_magic_number(123))
print(is_magic_number(1729))
print(f'{is_magic_number(250)}{"#*30"}')

"""24.  Scrivi una funzione che verifica
 se in una stringa le parentesi '(' e ')'
 sono bilanciate, cioè per ogni parentesi 
 che apre c'è la corrispondente parentesi che chiude.""" 

def check_parentheses(expression: str) -> bool:

    contatore= 0 
    for char in expression:
        if char == '(':
            contatore += 1 
        elif char == ')' :    
            contatore -= 1
        if contatore < 0:
            return False
    return contatore == 0


def check_parentheses1(expression: str) -> bool:

    contatore= 0 
    for char in expression:
        if char == '(':
            contatore += 1 
        elif char == ')' :    
            contatore += 1
        if contatore %2 == 0 :
            return True
        else:
            return False 
    
# def parentesi_bilanciate(s):
#     count = 0
#     for char in s:
#         if char == '(':
#             count += 1
#         elif char == ')':
#             count -= 1
#         # Se il contatore diventa negativo, le parentesi non sono bilanciate
#         if count < 0:
#             return False
#     # Alla fine, il contatore deve essere zero
#     return count == 0

# # Test della funzione
# print(parentesi_bilanciate("((()))"))  # Output: True
# print(parentesi_bilanciate("(()"))     # Output: False
# print(parentesi_bilanciate(")("))      # Output: False
# print(parentesi_bilanciate("(a + b) * (c - d)"))  # Output: True
# print(parentesi_bilanciate("((a + b)) + (c - d")) # Output: False


#Test della funzione
print(check_parentheses("((()))"))  # Output: True
print(check_parentheses("(()"))     # Output: False
print(check_parentheses(")("))      # Output: False
print(check_parentheses("(a + b) * (c - d)"))  # Output: True
print(check_parentheses("((a + b)) + (c - d")) # Output: False


 
"""25. Scrivi una funzione che conta quante volte 
un elemento appare isolato in una lista di numeri interi. 
Un elemento è considerato isolato 
se non è affiancato da elementi uguali."""

def roscio (l: list):

    posizione: int = 0
    diz: dict = dict()
    # for i in range(1,(len(l)-1)):
    #     print (i) 
    #     if i[1]== l[2]:
    for i in range(len(l)):
        print (i)
        if l[0] != l[1] and l[1] != l[2]:
            pass
            
        #if i !=  
        #     diz[i]= 1
        # return diz


l21= [1,1,2,3,4,5,6]
print (roscio(l21))
 


def roscio1 (l: list):

    diz = defaultdict(int)

    for i in range(0, len(l)): # cicla sugli indici di una lista [1,1,3,4,3,6,7,6,8]

        if i == 0: # se lelemnto i è 0 fai questo :
            if l[i] != l[i+1]: # se l che è 0 è diverso da l'elemnto sucessivo 
                diz[l[i]]= diz[l[i]]+1 # crea il dizionario con l'elemnto 0 
        elif i == (len(l)-1):
            if l[i] != l[i-1]:
                diz[l[i]]= diz[l[i]]+1
        else:
            if l[i] != l[i-1] and l[i] != l[i+1]:
                diz[l[i]]= diz[l[i]]+1
       
    return diz

lista = [1,1,3,4,3,6,7,6,8]
isolati = roscio1(lista)
print(isolati)



l= [34,5,6,7,10,14,23,47,1,1,1,2,2,2,3,3,3,3]
z = set(l)

print (z)
"""26. Scrivi una funzione chiamata create_contact() 
che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo). 
La funzione dovrebbe restituire un dizionario con i dettagli del contatto.

ESEMPIO: create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=69876543)

OUTPUT: {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 788787}

Scrivi una funzione chiamata update_contact() che accetta il dizionario creato,
 il nome e cognome del contatto da aggiornare, 
 e il dettaglio facoltativo da aggiornare. 
 Questa funzione dovrebbe aggiornare il dizionario del contatto.

ESEMPIO: update_contact(dict, "Mario Rossi", telefono=123456789)

OUTPUT: {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 123456789}
"""

def create_contact(nome: str, 
                cognome: str,
                 email: str= None, 
                 telefono: int = None) :
    contact: dict= {}
    contact['profile']= nome +(cognome)
    contact['email']= email
    contact['telefono']= str(telefono)

    return contact   

d=create_contact("Andrea ","Rossi")
print(d)

def update_contact( diz:dict,
                    set_name: str,
                    set_telefono: int,
                    setemail: str):
    
    diz["profile"]=set_name
    diz['email']= setemail
    diz['telefono']= str(set_telefono)

    return diz

print(update_contact(d,'Simo Cagliu', 2878824, 'fmio@gmail.com'))