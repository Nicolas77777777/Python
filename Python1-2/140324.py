#ho la stringa "123," la voglio trasformare in [1,2,3]

#definire una funzione che risolva il problema 

#def trali (x):

# fin= open("alice.txt","r")      #apri il file che si trova nella stessa cartella altrimenti scivere il percorso
#                                 #  r sta per lettura read 
# linee = fin.readlines()         #legge tutte le righe 
# fin.close()                     # chiude la variabile fin ( che apre il txt )

# l1=[]
# for l in linee:                 # si creato un ciclo 
#     l1.append(l.strip())

#     linee=l1
# print(linee)

# lista=[]
# for l in linee:
#      lista.append (l.split(""))


#print(lista)

def Maiuscula (c):
    return c.isupper()

s="Nel Cammin di Nostra Vita"

print(list(filter(Maiuscula,s)))


lista=[1,2,3,4,5,6,7,8]             #

def pari (n):
    return n %2 ==0

print(list(filter(pari, lista)))


ls=["uno"," ","due","tre"," ","" ,"","fine"]        # lista
lnuova=[]                                           #toglie gli spazi 
for i in ls:
    #if len (i.strip()) > 0:
    if i.strip() != "":
        lnuova.append(i)

print(lnuova)

#contare quanti caratteri ci sono in txt
#contare quanti caratteri non spazi bianchi ci sono in alice.txt
# contare quanti caratteri alfanumerici [a-zA- Z0-9] ci sono in alice.txt


fin= open("alice.txt","r")      #apri il file che si trova nella stessa cartella altrimenti scivere il percorso
                                #  r sta per lettura read 
linee = fin.readlines()         #legge tutte le righe 
fin.close()

print(len(linee))
print(len.alice.txt)

for sv in linee:
    spazibianchi=[]
    if len (sv.strip())==" ":
        spazibianchi.append(sv)

print(spazibianchi)

###############################################

