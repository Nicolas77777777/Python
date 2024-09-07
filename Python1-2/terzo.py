#a= print
#a("ciao come va")
#print=100
#a("ok")
#
a=10
print(type(a))

a=float
print(type(a))

a=a(3)
print

import random
import sys

a = 10
print(type(a))

a = float
print(type(a))

a = a(3)
print(type(a))

a = print
print(type(a))

#!!! and=10

# !! return = 100

ilmiocontatore = 10
ilMioContatore = 10

il_mio_contatore = 10

s_pippo = "aa"
i_pippo = 10
f_pippo = 3.3
c_pippo = "c"

"""
a=["v", "mm", "ppp"]
a inizia al posto 6

0  "mm" 
1  8
2
3
4
5
6 "v"
7 0
8 "ppp"
9 NULL
10
"""

lista = [1, 2, "tre", print, "ciao"]

print(lista[0])
print(lista[2])
lista[3](lista[4])

a = 10
b = 11
c = 12
print("il valore di a è ", a, "Il valore di b è ", b, "il valore di c è ", c)
print(f"il valore di a è {a}, Il valore di b è {b} il valore di c è {c}")


x, y, *z = "apple", "banana", "straberry", "orange"
print(x, y, z)

x, y, *z = ["apple", "banana", "straberry", "orange"]
print(x, y, z)

x, y, *z = ("apple", "banana", "straberry", "orange")
print(x, y, z)

lista = ["apple", "banana", "straberry", "orange"]
tupla = ("apple", "banana", "straberry", "orange")

print(lista[3])
print(tupla[3])

print(lista)
print(lista[2:])
print(lista[1:3])

print(lista[-1:])
print(lista[-2:])

l = [1, 2, 3, 4, 5, "sei" "sette", 8, [9, 10, 11], "dodici"]
for v in l:
    print(v)
print("fine")

for v in tupla:
    print(v)

for v in "Ciao come stai":
    print(v)


for i in range(10):
    print(i)

for i in range(4, 20, 3):
    print(i)

# Stampare la tabellina del 13
for i in range(13, 131, 13):
    print(i, end=" ")
print()

# a = range(100)
# print(a)

print(len("C i a o"))
print(len(tupla))
print(len([1, 2, 3, 4, 5, "a         ", 6, 5, 4, 3, 2, 1]))
a = [1]
a.append(2)
print(a)

a = "aaa"
b = "bbb"
c = a + b

a = [11, 22]

a.append(10)
print(a)

a.sort()
print(a)

print(a)
a.append(1000)
a.pop()
print(a)
print(sum(range(100)))
a = iter(range(100))
print(next(a))
print(next(a))
print(next(a))

# In una stanza entrano, uno dopo l'altro, 10 persone, rispettivamente:
# antonio, marco, andrea, luigi, tony, bruno, laura, anita, annarita, lucia
# le prime due vanno via dopo un pochino di tempo ma entrano altre tre persone
# john, alice, mary
# altre due vanno via, sempre in ordine di ingresso (primo entrato, primo a uscire)
# stampare l'elenco delle persone presenti
# per generare un numero casuale tra 10 e 20, 20 incluso: random.randint(10, 20)
# per generare un numero casuale tra 0 e 1: random.random()
#


# In una stanza entrano, uno dopo l'altro, 10 persone, rispettivamente:
room=["antonio", "marco", "andrea", "luigi", "tony", "bruno", "laura", "anita", "annarita", "lucia"]

print(room)
#####################

#le prime due vanno via dopo un pochino di tempo ma entrano altre tre persone ohn, alice, mary
room=room[2:]
room.extend(["john", "alice", "mary"])
print(room)

room=room[2:]
print(room)





