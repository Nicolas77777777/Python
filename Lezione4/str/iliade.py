text= open("iliade.txt", "r")
test = text.readlines()
text.close()

s = "Cantami, o Diva, del pelide Achille l'ira funesta che infiniti addusse lutti agli Achei, molte anzi tempo all'Orco generose travolse alme d'eroi, e di cani e d'augelli orrido pasto"

print(s[0])
print(s[1])


print(s[-1])


def counter(s: str) -> list:
    

    """" questa funzione prende una stringa in inpute 
    restituisce una lista costruita nel modo seguente:

    - il primo eleemnto della lista contiene il numero di caratteri nella stringa
    - il secondo contieene il numero di parole 
    - il terzo contiene il numero di parole distinte nella stringa
    - il quarto contiene il numero di frasi nella strnga"""

l: list [int]=[]
l[0] = len(s)

pass

# 2:15 video lezione 