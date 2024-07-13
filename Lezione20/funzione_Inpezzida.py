import math

def inPezzida(importo):
    banconote = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    how_many_banconote = {}

    for banconota in banconote:
        how_many_banconote[banconota] = int(importo // banconota)  # Usa divisione intera
        importo = round(importo % banconota, 2)  # Aggiorna l'importo con il resto e arrotonda a due decimali per evitare problemi di precisione
        print("quante banconote", how_many_banconote)

    for banconota, count in how_many_banconote.items():
        if count != 0:
            print(f"Banconota/Moneta: {banconota} - Quantità: {count}")


inPezzida(1024)