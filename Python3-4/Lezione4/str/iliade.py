# text= open("iliade.txt", "r")
# test = text.readlines()
# text.close()

s: str = "Cantami, o Diva, del pelide Achille l'ira funesta. Che infiniti addusse lutti agli Achei, molte anzi tempo all'Orco generose travolse alme d'eroi, e di cani e d'augelli orrido pasto"
x: str = "Ciao ciao Bello, cosa si dice, si dice tutto bene ciao ciao "

re= " tu dimmi quando quando, le mia mani mani faccia faccia "
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
    diz: dict = dict()
    a= s.lower()
    print(a)
    b= a.replace(',','')
    print(b)
    word = b.split()
    print(word)
   
    for parole in word:
        if parole  not in diz:
            diz[parole] = 1
        else:
            diz[parole] +=1

    filtro: dict [str:int ] = dict()

    for key in diz:
        if diz[key] > 1:
            filtro[key]=diz[key]

    return diz, filtro



    
    # word_wo_duplicate: set =set(s)
    # print (word_wo_duplicate)




print(word_count(x))
print(word_count(re))


# lower =x.lower()
# print(lower)
# vir=lower.replace(",","")
# print(vir)
# word = vir.split()
# print (word)

# senzaduplicati = set(word)
# print(senzaduplicati)
