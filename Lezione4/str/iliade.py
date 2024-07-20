# text= open("iliade.txt", "r")
# test = text.readlines()
# text.close()

s: str = "Cantami, o Diva, del pelide Achille l'ira funesta. Che infiniti addusse lutti agli Achei, molte anzi tempo all'Orco generose travolse alme d'eroi, e di cani e d'augelli orrido pasto"
x: str = "Ciao ciao Bello, cosa si dice, si dice tutto bene ciao ciao "
# print(s[0])
# print(s[1])


# print(s[-1])


# def counter(s: str) -> list:
#     """" questa funzione prende una stringa in inpute 
#     restituisce una lista costruita nel modo seguente:

#     - il primo eleemnto della lista contiene il numero di caratteri nella stringa
#     - il secondo contieene il numero di parole 
#     - il terzo contiene il numero di parole distinte nella stringa
#     - il quarto contiene il numero di frasi nella strnga"""

#     l: list [int]=[]
#     s.lower()
#     s.replace("."," ")
#     s.replace(","," ")
#     s.strip()
#     lenght=(len(s))
#     print()
#     l.append(lenght)
#     word= s.split()
#     print(word)
#     wordlen= len(s.split())
#     l.append(wordlen)
#     frasi= s.split(".")
#     print(frasi)

#     parole_distinte = set(word)

#     print(parole_distinte)



# counter(s)

# counter(x)

# z=x.strip(",")
# a=z.replace(","," ")
# ab=set(a)
# print(a)


def word_count (s: str) -> dict:

    s.lower()
    print(s)
    s.strip(',')
    print(s)
    # word_wo_duplicate: set =set(s)
    # print (word_wo_duplicate)




#word_count(x)


lower =x.lower()
print(lower)
vir=lower.strip(",")
print(vir)
