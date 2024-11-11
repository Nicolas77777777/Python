
# Per prima cosa leggiamo il file, essendo json utilizziamo le librerie JSON
import json

# Per leggere un file json
filejson = open(
    "all-world-cup-players.json",
    "r",
)
worldcup = json.load(filejson)
filejson.close()

print(type(worldcup))
print(type(worldcup[0]))


# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo

weee = []
# Per ogni calciatore....
# ho provato a selezionare l'elemento YEAR IMPOSTANDO LA CHIAVE VALORE SU 1934 1938 1942
for c in worldcup:
    if c["Year"] == 1930 :
        weee.append(c["DateOfBirth"])


# print(giovcalciatori)

# print(type(giovcalciatori))
############ fai lo split del primo elemento della lista e crea una lista ###
anni_nascita = []
for data in weee:
    if data != '':
        anno = int(data.split('-')[0])
        anni_nascita.append(anno)
        anni_nascitasenzadulpicati=list(set(anni_nascita))

print(anni_nascitasenzadulpicati)

#######per ogni elemeto della lista sottrai 1930
for meno in anni_nascitasenzadulpicati :
    y= 1930- meno

print("questo è il valore di ""Carvalho Leite",y) 

for meno in anni_nascita :
    z= 1930- meno

print("questo è il valore di z",z) 

weee = []
for c in worldcup:
    if c["Year"] == 1934 :
        weee.append(c["DateOfBirth"])

print(weee)

