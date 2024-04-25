import random

l=["c","i","a","o"]

for i in l:
    print(i)

for j in range(len(l)):
    print(l[j])

#prova con il while 
i=0 # counter esterno 
while i < len(l): #-> l=[0,1,2,3] #finche i è minore alla lunghezza della lista 
    print(l[i]) # scrivendo solo questo il ciclo è infinito 
    i += 1 # questo blocca il ciclo while perche la richiesta è stata soddisfatta

## scansione con dict

menu: dict = {"pasta": 10.50, "pizza": 9.00, "salad": 6.50,
"wine": 4.00, "water": 2.30}

for key in menu:
    print(f"chiave = {key} valore {menu[key]}")

#trasforma tutte le Key set in una lista/ idem per valori 

keys: list = list(menu.keys())
values: list = list(menu.values())

print( keys,values)

i=0
while i < len(keys):
    print(f"chiave = {keys[i]} {values[i]}")
    i+=1

# sapendo che la funzione random.randint(start, end)
# genera un numero intero compreso tra start e end, end compreso,
# costruire una lista di numeri casuali lunga 100 e
# stampare la somma di tutti i suoi numeri

def list_numeri_random (num_max: float,num_start: float, num_end: float):
    lnc = []
    for i in range(num_max):
        lnc.append(random.randint(num_start,num_end))
    return f"{lnc} {len(lnc)}"
   

print(list_numeri_random(60,-100,100))

print(list_numeri_random(100,-100,100))





def prova_if_else (x: float,y: float):
    l=[]
    if x > y:  
        res= x-y
        l.append(res)
        return f"{l} questo è se x è maggire di y addiziona"
    elif x < y:
        res= x+y
        l.append(res)
        return f"{l} questo è se x è minore di y addiziona"
    elif x==y:
        res= x**y
        l.append(res)
        return f"{l} questo è se x e y sono uguali"
    else:
        return f"non è possibile"
    

out= prova_if_else(-20,50 )
print(prova_if_else(10004444444,4554253535235325325))

print(out)







