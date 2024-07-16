# Scrivi una funzione che, dato un insieme 
# e una lista di numeri interi da rimuovere, 
# ritorni un nuovo insieme senza i numeri specificati nella lista.

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    new_set = original_set.copy()
    list_set= list(new_set)
    for elements in elements_to_remove:
        if elements in new_set:
            new_set.remove(elements)
    return new_set


print(f'{remove_elements({5, 6, 7}, [7, 8, 9])} \n')

# Scrivi una funzione che elimini dalla lista dati certi elementi
# specificati in un dizionario. Il dizionario contiene elementi 
# da rimuovere come chiavi e il numero di volte che devono
# essere rimossi come valori.


def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:

    for key, value in da_rimuovere.items():
        if key in lista:
            
            lista.remove(key)

    return lista  

####altro esempio 

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

# Scrivi una funzione che determina se un numero è 'magico'. 
# Un numero è considerato magico se è divisibile per 4 ma non per 6.

def numero_magico(num: int) -> bool:
    if num % 4==0 and num % 6 != 0:
        return True
    else:
        return False
    
print(numero_magico(8))

print(numero_magico(12))

print(numero_magico(16))

print(numero_magico(24))

print(numero_magico(28))

# Scrivi una funzione che prenda in input una
# lista di dizionari che rappresentano
# voti di studenti e aggrega i voti 
# per studente in un nuovo dizionario.

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


# Scrivi una funzione che elimini dalla lista dati certi elementi
# specificati in un dizionario. Il dizionario contiene elementi 
# da rimuovere come chiavi e il numero di volte che devono
# essere rimossi come valori.


def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:

    for key, value in da_rimuovere.items():
        if key in lista:
            for i in range(value):
            
                lista.remove(key)

    return lista 



print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
print(rimuovi_elementi([], {2: 1})) 
print(rimuovi_elementi([3,3,3,3,3,3,3],{3:3,4:3}))