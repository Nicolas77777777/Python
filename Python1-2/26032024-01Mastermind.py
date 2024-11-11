# il gioco del master mind consiste in:
# N palline colorate (i nostri digit)
# M caselle da riempire (la lunghezza delle nostre liste)
# una sequenza di M palline colorate generata dal master del gioco
# un ciclo di prove in cui
#   1) il giocatore fornisce la sua proposta
#   2) il master verifica il numero di strike e ball ottenuti
#   3) il master comunica strike e ball al giocatore
#   4) se sono M strike, il giocatore ha vinto
#       5) altrimenti si riparte da 1, con la nuova proposta
# Esempio di gioco
#   N=6 (sei simboli, da 1 a 6)
#   M=4 (lunghezza delle liste pari a 4)
#   master= GeneraLista(4, 6)
# quindi master potrebbe essere ad esempio [4,1,1,5]
# ciclo di gioco
#     1) il giocatore comunica "1234" che viene trasformato in [1,2,3,4]
#     2) [1,2,3,4] vs [4,1,1,5] => 0 strike, 2 ball
#     3) non ha vinto poichè servono M strike
#     4) il giocatore ricomincia al punto 1, stavolta,
#        ovviamente, con una nuova proposta, es 2156 => [2,1,5,6]
#     ecc, ecc, ecc




import copy
import random


# Genera una lista che contiene M numeri casuali tra 1 e N
def GeneraLista(N, M):
    lista = []
    for i in range(M):
        v = random.randint(1, N)
        lista.append(v)
    return lista


def ContaUgualiInStessoEInAltro(ls, lsCheck):
    ls = ls.copy()
    lsCheck = lsCheck.copy()
    # Conteggio e elimino gli elementi nello stesso posto
    stessoPosto = 0
    for i in range(len(lsCheck)):
        if lsCheck[i] == ls[i]:
            stessoPosto += 1
            ls[i] = None
            lsCheck[i] = None

    # Conteggio e elimino gli elementi in posto differente
    altroPosto = 0
    for v in lsCheck:
        if v != None and v in ls:
            altroPosto += 1
            ls.remove(v)
    return stessoPosto, altroPosto


N = int(input("Inserire il numero di simboli: "))
M = int(input("Inserire la lunghezza della lista: "))
# l1 = GeneraLista(N, M)
# l2 = GeneraLista(N, M)
# print(l1)
# print(l2)
# strike, ball = ContaUgualiInStessoEInAltro(l1, l2)
# print(strike, ball)
# print(l1)
# print(l2)


def ConvertiStringaDigitInListaNumeri(sd):
    return [int(x) for x in list(sd)]


# # Esempio di utilizzo:
# sd = input("Inserisci la tua prova: ")
# print(ConvertiStringaDigitInListaNumeri(sd))



segreto=GeneraLista(N,M)

while True:
    proposta = input("Utente inserirci la tua proposta: ")
    # Devo far diventare la proposta una lista 
    proposta=ConvertiStringaDigitInListaNumeri(proposta)
    strike, ball=ContaUgualiInStessoEInAltro(proposta, segreto)
    print("Strike: ", strike, "Ball: ", ball)
    if strike == M:
        print("BRAVO HAI VINTO")
        break


    