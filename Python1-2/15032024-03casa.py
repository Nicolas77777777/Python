import json

#Per leggere un file json 
filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()

print(len(worldcup))

print(("1200 elemento"),worldcup[1200],worldcup[1])
print(type(worldcup))
print(worldcup[1200]['DateOfBirth'])




# !!!! SONO TUTTE OPERAZIONI SU LISTE !!!!
# 1) contare quanti calciatori hanno giocato per l'Italia
# 2) contare quanti calciatori hanno giocato per il Brasile
# 3) contare quanti calciatori hanno giocato per l'Argentina
# 4) Indicare quali calciatori hanno giocato sia per il Brasile, sia per l'Italia
# 5) Indicare quali calciatori hanno giocato sia per l'Argentina, sia per l'Italia
# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo
# 7) Trovare qual'è il calciatore più anziano che ha partecipato alla coppa del mondo
# 8) Trovare quale calciatore ha partecipato a più edizioni della coppa del mondo
# 9) Trovare quale squadra di calcio ha fornito più calciatori per la coppa del mondo
#    Organizzare per nazione. Cioè quale squadra italiana ha fornito più calciatori per la coppa del mondo e quanti, quale squadra francese, ...

#Esempio:
quantiCalciatori = dict()
for v in worldcup:
    # se v.Team è già presente, sommo 1, altrimenti metto a 1
    if v["Team"] in quantiCalciatori.keys():
        quantiCalciatori[v["Team"]]=quantiCalciatori[v["Team"]]+1
    else:
        quantiCalciatori[v["Team"]]=1

print(quantiCalciatori)
print(type(quantiCalciatori))               # ho stampato quanticalciatori per essere sicuro che fosse un dizionario
    
ck= quantiCalciatori.keys()
cv= quantiCalciatori.values()

print(ck)
print(cv)

# if 'Italy ' in quantiCalciatori:
#   print("Yes, 'Italy' is one of the keys in the thisdict dictionary") 

calciatItalia=quantiCalciatori['Italy']
print(("1) contare quanti calciatori hanno giocato per l'Italia"),(calciatItalia))

calciatBrasile=quantiCalciatori["Brazil"]
print(("2) contare quanti calciatori hanno giocato per il Brasile"),(calciatBrasile))

calciatArgentina=quantiCalciatori["Argentina"]
print(("3) contare quanti calciatori hanno giocato per l'Argentina"),(calciatArgentina))



# #6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo
youngCalciatori = dict()
for g in worldcup:
    # se v.Team è già presente, sommo 1, altrimenti metto a 1
    if g["DateOfBirth"] in youngCalciatori.keys():
        youngCalciatori[g["DateOfBirth"]]=youngCalciatori[g["DateOfBirth"]]+1
    else:
        youngCalciatori[g["DateOfBirth"]]=1
    
print(youngCalciatori)


youngCalciatori_Year = dict()
for y in worldcup:
    # se v.Team è già presente, sommo 1, altrimenti metto a 1
    if y["Year"] in youngCalciatori_Year.values():
        youngCalciatori_Year[y["Year"]]=youngCalciatori_Year[y["Year"]]+1
    else:
        youngCalciatori_Year[y["Year"]]=1
    
print(youngCalciatori_Year)

print(youngCalciatori_Year.keys())
print(youngCalciatori_Year.values())

print(type(worldcup))
# worldcup=dict()
# print(type(worldcup))

# print(worldcup.keys())
#print(worldcup)

###1930, 1934, 1938, 1950, 1954, 1958, 1962, 
##1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014])










        
