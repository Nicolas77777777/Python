# progetto segmentato 

# sia data una lista <ls> contenente N digit da 1 a N 
#non necessariamente tutti presenti quini con 
# eventuali ripe
 #se il valore N è 4 ci devono essere 4 argomenti ex 1,1,2,2

#sia data una seconda lista costruita come la precedente, ovviamente 
#con valori diversi ma sepre nel rispetto del valore N lscheck

#scrivere una fuzione dove passerete i parametri ls lschek 
#e la funzione deve riportare due valori:

#il primo tutte le volte che 

import random

# ls=[1,5,4,3,3,6,1]
# lsCheck=[4]



def Generalista (n):
    elenconumeri=[]
    for i in range(n):
        elenconumeri.append(random.randint(1,n))
    
    return elenconumeri


print(Generalista(10))
print(Generalista(10))

# def Contauguali (ls,lsCheck):
#     elementiUGposizione=[]
#     for i in lsCheck:
#         if i[:10]== ls[:10]+ 1:
#         else

# for i in range(8):
#     print(i)

def Contauguali (ls,lsCheck):
    uguali=0
    for i in range(len(ls)):     #range (len lunghezza dell'index
        if ls[i]==lsCheck[i]:
            uguali=uguali+1
    return uguali 
   
n=9
l1= Generalista(n)
l2= Generalista(n)

print(l1)
print(l2)

print(Contauguali(l1,l2))


def ContaUgualiInAltroPosto (ls,lsCheck):
    es=[1,2,3,4,5,6]


    