# creare un dizionario 
diz1: dict = {"Nome":"Franco","Cognome": "Rossi"}

diz2: dict = dict(Name= "Jhonny",Surname="Permaloso") # con il costruttore

x = diz1["Nome"] # accedere alle chiavi del dizionario tramite  inside square brackets

y_get = diz2.get("Name") # accedere alle chiavi del dizionario tramite get 

k2= diz2.keys() # mette le chiavi in una lista

k1= diz1.keys()

v1=diz1.values()

diz1["eta"]= 31

diz2["age"]= 45


print(f'\n{diz1} \n-------\n{diz2}\n')

print(f'{len(diz1)}\n , {x}, {y_get} \n{k2}\n{v1}\n')

print(f' accede alla chiave ed al valore x {x},\n {y_get}\n {k2}')

print(f' accede alla chiave ed al valore con get {y_get} {k2}')

diz2["age"]= 430

print(f'\n{diz1} \n-------\n{diz2}\n')

z1= diz1.items()

print(z1)

if "age" in diz2:
    print (True)


if diz2.values() == 0: 
    print (True)

else:
    print (False)
    