#Verifica conoscenze sulle funzioni

# Scrivi una funzione somma_elementi(x: list[int], y: list[int]) -> list[int] 
# che calcola la somma elemento per elemento di due liste x e y e restituisce il risultato.

def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    res: list = []
    if len(x)  == len(y):
        for i in range(len(y)):
            som=x[i]+y[i]
            res.append(som)
        return res
    else:
        len(x) != len(y)
        z: list = x[0]+y[0]
        res.append(z)
    return res

print(f" sommma liste {somma_elementi([-18,2,4,5,1,10,12,45,-1,0,45,0,0,0,0,0],\
                                    [-18,92,91,0,12,-1,48,53,0,0,0,0,-1,7])}")

print(somma_elementi([1,],[1,2]))
print(somma_elementi([1,1,1],[1,1,1]))

# Scrivi una funzione prime_factors(n: int) -> list[int] che trova 
# i fattori primi di un numero n dato in input

# def prime_factors(n: int):
#     numeriprimi=[]
#     while n > 1 :
#         if n % 2:
#             n1= n %2
#             numeriprimi.append(n1)
#         pass

# print(prime_factors(4))


# Nel gioco del blackjack, il valore di una mano è determinato dalla somma dei valori delle carte. 
# Ogni carta ha un valore compreso tra 2 e 11 compresi. Tuttavia, se una mano contiene un asso,
# il valore dell'asso può essere 1 o 11, a seconda di quale sia più favorevole al giocatore in 
# quel momento. Dato un elenco di valori delle carte che 
# rappresentano una mano di blackjack, scrivi una funzione per determinare il valore totale della mano.

def blackjack_hand_total(cards: list[int]) -> int:
    somma: int = 0
    blackjack: int = 21
    asso= 1
    for i in cards:
        somma= i+ somma

    if somma == blackjack:
        return somma
    
    elif somma != blackjack:
        return somma
        
    elif asso in cards and somma > blackjack:
        
        return somma
    elif asso in cards and somma < blackjack:
        for asso in cards:
            asso=11
            somma= i+somma
        
        return somma

        #     if somma < blackjack:
        #         asso=11
        #         return somma
        #     elif somma > 21: 
        #         asso=1
        #         return somma
            
print((blackjack_hand_total([2, 3, 5,23])))
print(blackjack_hand_total([1, 3, 5]))
print(blackjack_hand_total([1, 3, 5,3]))



#[-36, 94, 95, 5, 13, 9, 60, 98, -1, 0, 45, 0, -1, 7]
# def const (area: float):
#     l: int = area/2
#     w: int = area/2
#     li,wi=int(l),int(w)
#     list_w_l:list= [li,wi]
   
#     return list_w_l


#print(const(4))


# def even_odd_pattern1(nums: list[int]) -> list[int]:
#     pari=[]
#     dispari=[]
#     for i in nums:
#         if i % 2==0:
#             pari.append(i)
#         elif i % 2 !=0:
#             dispari.append(i)
        
#     return pari + dispari

# print(even_odd_pattern1([3, 6, 1, 8, 4, 7]))
    
