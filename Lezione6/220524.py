
from math import sqrt


"""Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1 """

def transform(x: int) -> int:

    if x %2 == 0 :
        return x//2
    
    else:
        x % 2 != 0 
        return x*3-1
    

print(transform(4))
print(transform(-10))



"""" Sviluppare una funzione in Python per calcolare lo stipendio
 lordo di ciascuno dei diversi impiegati. L'azienda paga 10 dollari
all'ora per le prime 40 ore di lavoro e paga "una volta e mezza"
la paga oraria per tutte le ore di lavoro oltre le 40 ore.
 
Per ogni operaio, viene fornito il numero di ore che tale impiegato
 ha lavorato durante la settimana.
La vostra funzione deve ricevere questa informazione per ogni impiegato e
 determinare e stampare lo stipendio lordo."""


def calcola_stipendio(ore_lavorate: int) -> float:
    stipendio_lordo: int =  0
    ore_normali = 40 
    if ore_lavorate <= ore_normali :
        stipendio_lordo =  ore_lavorate *10
        return  stipendio_lordo
    if ore_lavorate > ore_normali:
     ore_straordinarie = ore_lavorate - ore_normali
     nstipendio_lordo = 40*10 + ore_straordinarie*15
    
    return nstipendio_lordo
    

print(calcola_stipendio(40))
print(calcola_stipendio(0))

print(calcola_stipendio(60))
                

    

def hypotenuse(a: float, b: float):
    hypotenuse= sqrt( a**2 + b**2)
    
    return hypotenuse



print(hypotenuse(3.0, 4.0))




for i in range(1,8):
    print(i)


for i in range(3,24,5):
    print(i)


for i in range(20,-12,-6):
    print(i)



for i in range(19,51,8):
    print(i)




def integerPower(base, esponente):

    return base **esponente

def seconds_since_noon(ore:int ,minuti: int ,secondi: int):








