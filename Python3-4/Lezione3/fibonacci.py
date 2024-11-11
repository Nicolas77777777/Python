def fibonacci (numero:int) :
    if numero <= 2:
        return 1
    else:
        return fibonacci(numero-1)+ fibonacci(numero-2)
    
fibonacci(10)


def fibonacci_for(numero: int):
    memoria: list = [1,1]
    for i in range(1,numero):
        risultato: int = memoria[i-1]+memoria[i]
        memoria.append(risultato)
    return memoria[-1]

print(fibonacci_for(60))


def fibonacci4 (i:int): 
    a= 1
    b=1

    for i in range (i):
        c = a+b
        a = b
        b = c

    return b

import time

a = time.time()

print(f'tempo impiegato {time.time()- a} ')

print(fibonacci4(51))
print(fibonacci4(2))
