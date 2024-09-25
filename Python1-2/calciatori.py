# !!!! SONO TUTTE OPERAZIONI SU LISTE !!!
# Il problema. Cosa fare?
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

# Cosa fare?
"""
1) leggere i dati (importare i dati nel programma)
2) organizzare i dati in modo opportuno (nel nostro caso sono già organizzati come elenco di calciatori, con un insieme di proprietà per ogni calciatore)
3) per ogni richiesta il cosa constiste in un conteggio oppure nella ricerca di condizioni specifiche
"""

# Per prima cosa leggiamo il file, essendo json utilizziamo le librerie JSON
import json

# Per leggere un file json
filejson = open(
    "all-world-cup-players.json",
    "r",
)
worldcup = json.load(filejson)
filejson.close()

"""
al simbolo worldcup ho associato una lista (la json.load) torna un elemento json che in questo caso corrisponde a una lista (delimitato da [])
"""
# Di che tipo è worldcup?
# Di che tipo sono gli elementi di worldcup?
print(type(worldcup))
print(type(worldcup[0]))

# exit(-1) # per non eseguire le istruzioni successive

# 1) contare quanti calciatori hanno giocato per l'Italia
# come? per ogni calciatore (cioè per ogni elemento della lista wordcup), se il calciatore appartiene al team ITA, lo conteggio
# Variabili? totaleCalciatoriItalia

# Inizializzo il contatore a 0
totaleCalciatoriItalia = 0
# Per ogni calciatore....
for c in worldcup:
    # devo verificare che il team sia ITA oppure Italy
    # if c["Team"] in ["ITA", "Italy"]:
    if c["Team"] == "ITA" or c["Team"] == "Italy":
        totaleCalciatoriItalia += 1
# Ho sbagliato, non ho tenuto conto dei requisiti!! Voglio solo i calciatori "diversi" invece in questo modo ho contato i duplicati
"""
Quindi dovrò
1) prendere tutti i calciatori che hanno giocato per l'italia
2) eliminare i duplicati
3) contare i duplicati
"""
calciatoriItalia = []
# Per ogni calciatore....
for c in worldcup:
    # devo verificare che il team sia ITA oppure Italy
    if c["Team"] in ["ITA", "Italy"]:
        # if c["Team"] == "ITA" or c["Team"] == "Italy":
        calciatoriItalia.append(c["FullName"])
calciatoriItaliaSenzaRipetizioni = set(calciatoriItalia)
print("Calciatori italiani: ", len(calciatoriItaliaSenzaRipetizioni))


# 2) contare quanti calciatori hanno giocato per il Brasile
calciatoriBrasile = []
for c in worldcup:
    if c["Team"] in ["BRA", "Brazil"]:
        calciatoriBrasile.append(c["FullName"])
calciatoriBrasileSenzaRipetizioni = set(calciatoriBrasile)
print("Calciatori brasiliani: ", len(calciatoriBrasileSenzaRipetizioni))

# 3) contare quanti calciatori hanno giocato per l'Argentina
# trivial!!!


# Ora al posto di fare sostanzialmente tre volte lo stesso codice, potrei scrivere una funzione
def ContaCalciatoriSquadra(elenco, squadra):
    calciatoriSquadra = []
    for c in elenco:
        if c["Team"] in squadra:
            calciatoriSquadra.append(c["FullName"])
    calciatoriSquadraSenzaRipetizioni = set(calciatoriSquadra)
    return len(calciatoriSquadraSenzaRipetizioni)


print("Calciatori italia: ", ContaCalciatoriSquadra(worldcup, ["ITA", "Italy"]))
print("Calciatori brasile: ", ContaCalciatoriSquadra(worldcup, ["BRA", "Brazil"]))
print("Calciatori argentina: ", ContaCalciatoriSquadra(worldcup, ["ARG", "Argentina"]))


# 4) Indicare quali calciatori hanno giocato sia per il Brasile, sia per l'Italia
""" come?
1) ottengo l'elenco dei calciatori che hanno giocato per l'italia
2) ottengo l'elenco dei calciatori che hanno giocato per il brasile
3) per ogni calciatore che ha giocato per l'italia
    verifico se è presente nell'elenco dei calciatori che hanno giocato per il brasile
"""


# Se modifico la funzione ContaCalciatoriSquadra e tolgo la len, ottengo esattamente
# l'elenco dei giocatori che hanno giocato in una certa squadra
def CalciatoriSquadra(elenco, squadra):
    calciatoriSquadra = []
    for c in elenco:
        if c["Team"] in squadra:
            calciatoriSquadra.append(c["FullName"])
    calciatoriSquadraSenzaRipetizioni = set(calciatoriSquadra)
    return calciatoriSquadraSenzaRipetizioni


calciatoriItalia = CalciatoriSquadra(worldcup, ["ITA", "Italy"])
calciatoriBrasile = CalciatoriSquadra(worldcup, ["BRA", "Brazil"])
calciatoriArgentina = CalciatoriSquadra(worldcup, ["ARG", "Argentina"])

print("Calciatori italia e brasile: ", calciatoriItalia.intersection(calciatoriBrasile))
print(
    "Calciatori italia e argentina: ",
    calciatoriItalia.intersection(calciatoriArgentina),
)

# # {1,2,3,4} intersezione {3,2,9,7,6,5} => {2,3}
# s1 = set([1, 2, 3, 4])
# s2 = set([3, 2, 9, 7, 6, 5])
# print(s1.intersection(s2))

# int("12345") => 12345
# set(x) => trasforma x in un set
# list(x) trasforma x in una lista

# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo
# 7) Trovare qual'è il calciatore più anziano che ha partecipato alla coppa del mondo
elenco_eta_calciatore = []
for calciatore in worldcup:
    anno_campionato = calciatore["Year"]
    anno_nascita = calciatore["DateOfBirth"].split("-")[0]
    if anno_nascita != "":  # elimino anni non presenti
        eta = anno_campionato - int(anno_nascita)
        elenco_eta_calciatore.append((eta, calciatore))

# print(elenco_eta_calciatore)
# devo trovare il più giovane e il più vecchio
etamax = 0
etamin = 200
cmax = None
cmin = None
for c in elenco_eta_calciatore:
    if c[0] < etamin:
        etamin, cmin = c
        # etamin=c[0]
        # cmin=c[1]
    if c[0] > etamax:
        etamax, cmax = c
print(cmin, cmax)

# 8) Trovare quale calciatore ha partecipato a più edizioni della coppa del mondo
# posso usare fullname concatenato a date of birth
calciatori = dict()
# come risultato vorrei in dizionario che come chiave ha il nome del calciatore e come valore ha quante il calciatore è presente nell'elenco
for c in worldcup:
    key = c["FullName"] + ":" + c["DateOfBirth"]
    if key in calciatori.keys():
        calciatori[key] = calciatori[key] + 1
    else:
        calciatori[key] = 1

massimo = 0
calciatore = None
for chiave, valore in calciatori.items():
    if chiave.split(":")[0] != "":
        if valore > massimo:
            massimo = valore
            calciatore = chiave
print(massimo, calciatore)

# 9) Trovare quale squadra di calcio ha fornito più calciatori per la coppa del mondo
#    Organizzare per nazione. Cioè quale squadra italiana ha fornito più calciatori per la coppa del mondo e quanti, quale squadra francese, ...
squadre = dict()
for c in worldcup:
    if c["Club"] in squadre.keys():
        squadre[c["Club"]] += 1
    else:
        squadre[c["Club"]] = 1

massimo = 0
squadra = None
for s in squadre.items():
    if s[1] > massimo:
        squadra, massimo = s
print(massimo, squadra)
