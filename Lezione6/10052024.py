# Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, 
# ritorni un nuovo insieme senza i numeri specificati nella lista


def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    # cancella pass e scrivi il tuo codice
    # for i in enumerate(original_set):
    original_set_new = list(original_set)

    for i in original_set_new:
        if i in elements_to_remove:
            
            print( original_set_new)

    # return type(elements_to_remove,elements_to_remove)
    

print(remove_elements({5, 6, 7}, [7, 8, 9])) #result {5,6}


    
    


# result {5,6}



# Scrivi una funzione che determina se un numero è 'magico'. 
# Un numero è considerato magico se è divisibile per 4 ma non per 6

def numero_magico(num: int) -> bool:
    # cancella pass e scrivi il tuo codice
    if num % 4 ==0 and num %6 !=0:
        return True
    
    else:
        return False
    

print(numero_magico(44))
