def change_keys_with_sum(d: dict[str, int], sum: float ) -> dict [str,float]:
    """"
    questa funzione cambia i valoridel dizionario d col 
    rapporto di essi con la somma sum

    """
    out ={}
    for key in d:
        out[key] = d[key] /sum

    return out 

def custom_sum(d: dict[str, int]) -> float:
    return sum(list(d.values()))

def rewrite_dict(d:dict[str,int]) -> dict[dict, float]:
    """" questa funzione prende in input un dizionario
    (e.s d- {"ciao" :2, "hello: 3}) e restituisce
    un nuovo dizionario fatto cosi:
    d1 ={"ciao : 275, "hello : 3/5} dove 5 è la somma 
    dei valori di d, ossia 2+3 =5"""
    

    print(f'il dizionario di input è {d}')
    somma= custom_sum(d)
    out: dict[str, float]= change_keys_with_sum(d,somma)
    return out 

d = {"ciao": 2, "hello": 3}
output = rewrite_dict(d)
print (f"il nuovo dizionario è { output }")

