from ast import main
import random


def create_list(num_elemnts: float, first_element: float, last_element:float) -> list[float]:

    l1 = [] # creo una lista vuota
    for i in range(num_elemnts): # con una linghezza massima num  elementi 
        l1.append(random.randint(first_element,last_element)) # aggingi gli elementi random di numeri tra 0 e 1000

    return l1




##########

    

l1=[1,2,3,[3,3,[5,6,7],3,3],4,5,6,7,8,9,10]

print(l1[3][2][0])

fra= "Fai attenzione ai tuoi nemici, perché sono i primi a scoprire i tuoi errori. "

fra.lower()
print(fra)
# print(fra.split("a"))

# print(fra.split("a"))
# print(fra.split("\n"))
# print(fra.strip(""))











