#  """Questa funzione prende in input un dizionario 
# es. d={"ciao:2,"hello:3} e restituisce un nuovo
# dizionario fatto cosi 
# d1 = {"ciao": 2/5, " hello": 3/5 è la somma dei valori di d,ossia 2+3= 5}"""


def change_keys_with_sum

dizio= {"ciao" : 2,"hello" : 3}
def rewrite_dic(d:dict[str,int]) -> dict[str, int]:
    somma= sum (list(d.values()))
    out= {}
    for key in d:
        out[key]= d[key] / somma

    return out

d={}
