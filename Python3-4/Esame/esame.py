#QUESTION1
"""
Scrivi una funzione che moltiplica tutti i 
numeri interi di una lista che sono 
minori di un dato valore intero definito threshold.
"""
def moltiplica_numeri(numbers: list[int], threshold: int) -> int:
   z: int = 1
   for numero in numbers:
       if numero < threshold:
           return z* numero

print(moltiplica_numeri([1, 10, 20, 30], 30))  # 200
print(moltiplica_numeri([15, 5, 25], 20)) # 75
print(moltiplica_numeri([3, 5, 8], 10)) # 120
print(moltiplica_numeri([50, 60, 70], 25)) # 1
print(moltiplica_numeri([2, 5, 1], 1)) # 1


#QUESTION2
def trova_tutte_chiavi(dizionario: dict[str: int], valore: int) -> str:
   
    """
    Scrivi una funzione che prenda un dizionario
     e un valore, e ritorni una lista con tutte 
     le chiavi che corrispondono a quel valore,
       o una lista vuota se il valore non è presente.
    """

    print(trova_tutte_chiavi({'a': 1, 'b': 2, 'c': 1}, 1)) # ['a', 'c']
    print(trova_tutte_chiavi({}, 1)) #[]

#QUESTION3
"""
Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:

a) 2, 4, 6, 8, 10, 12, 14
b) 1, 4, 7, 10, 13
c) 30, 25, 20, 15, 10, 5, 0
d) 5, 15, 25, 35, 45


"""  
