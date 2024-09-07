# Problema: ho la stringa "123", la voglio trasformare in [1, 2, 3]
# definire una funzione che risolva il problema
def Converti(s):
    usaMetodo1 = False
    if usaMetodo1:
        # metodo 1 (comprehension)
        return [int(c) for c in s]
    else:
        # metodo 2, for
        l = list(s)
        l1 = []
        for i in l:
            l1.append(int(i))
        return l1


print(Converti("192619263183"))

###############################

fin = open("alice.txt", "r")
linee = fin.readlines()
fin.close()

# readlines legge tutte le righe incluso il carattere a capo (eol/eoln)
# Come faccio a togliere questi fine riga?
l1 = []
for l in linee:
    l1.append(
        l.strip()
    )  # elimina spazi, tab e eol ma solo a inizio e fine della stringa
linee = l1
print(linee)


s = "alfa;beta;gamma"
# Come posso ottenere la lista ["alfa", "beta", "gamma"]?
print(s.split(";"))


# Dato alice.txt, stampare, una per riga, tutte le parole che la compongono
def Maiuscola(c):
    return c.isupper()


s = "Nel Mezzo del Cammin Di Nostra vita"
print(list(filter(Maiuscola, s)))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def Pari(n):
    return n % 2 == 0


print(list(filter(Pari, lista)))

# Data una lista di stringhe, eliminare dalla lista tutte le stringhe vuote
ls = ["uno", "", "due", "tre", "", "", "", " ", "  ", "fine"]
lnuova = []
for i in ls:
    if len(i) > 0:
        lnuova.append(i)

print(lnuova)

######################################################
# Contare quanti caratteri ci sono in alice.txt
# Contare quanti caratteri non spazi bianchi ci sono in alice.txt
# Contare quanti caratteri alfanumerici[a-zA-Z0-9] ci sono in alice.txt

fin = open("alice.txt", "r")
alice = fin.read()
fin.close()
print("Caratteri: ", len(alice))

fin = open("alice.txt", "r")
linee = fin.readlines()
fin.close()
caratteri = 0
for linea in linee:
    caratteri += len(linea)

print("Caratteri: ", caratteri)


fin = open("alice.txt", "r")
alice = fin.read()
fin.close()
notblank = 0
for c in alice:
    if c != " ":
        notblank += 1

print("Caratteri non blank: ", notblank)


fin = open("alice.txt", "r")
alice = fin.read()
fin.close()
alfanum = 0
for c in alice:
    if c.isalnum():
        alfanum += 1

print("Caratteri alfanumerici: ", alfanum)


fin = open("alice.txt", "r")
alice = fin.read()
fin.close()
alfanum = 0
for c in alice:
    if c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        alfanum += 1

print("Caratteri alfanumerici: ", alfanum)
