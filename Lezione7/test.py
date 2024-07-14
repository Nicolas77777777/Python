# Scrivi una funzione che, dato un insieme 
# e una lista di numeri interi da rimuovere, 
# ritorni un nuovo insieme senza i numeri specificati nella lista.

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    new_set: set  = []
    newlist=list(original_set)
    for i in newlist:
       if i in elements_to_remove:
            newlist.remove(i)
            new_set =set(newlist)

    return new_set
    
print(remove_elements({5, 6, 7}, [7, 8, 9]))
print(remove_elements({5, 6, 7,6}, [7, 8, 9,6,7])) # sbagliato non utilizzare discard

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