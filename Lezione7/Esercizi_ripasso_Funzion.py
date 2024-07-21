#QUESTION 1
"""Scrivi una funzione che, dato un insieme 
e una lista di numeri interi da rimuovere, 
ritorni un nuovo insieme senza i numeri specificati nella lista."""

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    new_set = original_set.copy()
    list_set= list(new_set)
    for elements in elements_to_remove:
        if elements in new_set:
            new_set.remove(elements)
    return new_set

print(f'{remove_elements({5, 6, 7}, [7, 8, 9])} Question1\n')

#QUESTION 2
"""Scrivi una funzione che determina se un numero
 è 'magico'. Un numero è considerato magico 
 se è divisibile per 4 ma non per 6."""

def numero_magico(num: int) -> bool:

    if num % 4 == 0 and num %6 != 0:
        return True
    else:
        return False

print(numero_magico(8))
print(numero_magico(12))
print(numero_magico(16))
print(numero_magico(24))
print(f'{numero_magico(28)} question 2 \n')

# QUESTION 3
"""Scrivi una funzione che elimini dalla lista dati certi elementi
specificati in un dizionario. Il dizionario contiene elementi 
da rimuovere come chiavi e il numero di volte che devono
essere rimossi come valori."""

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:

    for key, value in da_rimuovere.items():
        if key in lista:
            
            lista.remove(key)

    return lista  

# Altro esempio

def remove_elements2(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    # Creiamo un nuovo insieme partendo dall'originale
    new_set = original_set.copy()
    
    # Rimuoviamo ogni elemento della lista dall'insieme
    for element in elements_to_remove:
        if element in new_set:
            new_set.remove(element)
    
    return new_set

print(remove_elements2({5, 6, 7}, [7, 8, 9]))
print(remove_elements2({5, 6, 7,6}, [7, 8, 9,6,7]))

# altro esempio 

def rimuovi_elementi1(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:

    for key, value in da_rimuovere.items():
        if key in lista:
            for i in range(value):
            
                lista.remove(key)

    return lista 

print(rimuovi_elementi1([1, 2, 3, 2, 4], {2: 2}))
print(rimuovi_elementi1([], {2: 1})) 
print(rimuovi_elementi1([3,3,3,3,3,3,3],{3:3,4:3}))


# QUESTION 4
"""Scrivi una funzione che prenda in input una
lista di dizionari che rappresentano
voti di studenti e aggrega i voti 
per studente in un nuovo dizionario."""

def aggrega_voti(voti: dict) -> dict[str:list[int]]:
    new_dict = {}
    for elemento in voti:
        nome = elemento['nome']
        voto = elemento['voto']

        if nome in new_dict:
            new_dict[nome].append(voto)
        else:
            new_dict[nome]=[voto]
    return new_dict

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, 
                    {'nome': 'Bob', 'voto': 75},
                      {'nome': 'Alice', 'voto': 85}]))

#QUESTION 5
""" Scrivi una funzione che accetti un dizionario di prodotti 
con i prezzi e restituisca un nuovo 
dizionario con solo i prodotti che hanno un prezzo 
superiore a 20, scontati del 10%."""

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    # cancella pass e scrivi il tuo codice
    newdict: dict = {}
    for key,value in prodotti.items():
        if value > 20.0:
            sconto = (value *10) / 100
            newdict[key]= value - sconto

    return newdict


print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0}))

#QUESTION6 	
"""
PARTE 1
Scrivi una funzione chiamata create_contact() che accetta il nome e cognome,
 e-mail (facoltativo) e numero di telefono (facoltativo). 
 La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
 
PARTE 2
Scrivi una funzione chiamata update_contact()
 che accetta il dizionario creato, il nome e cognome
del contatto da aggiornare, e il dettaglio facoltativo 
da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.

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


