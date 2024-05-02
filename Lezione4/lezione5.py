# set insieme

# Scrivi una funzione che, dato un numero intero,
# determina se è un "numero magico".
# Un numero magico è definito come un 
# numero che contiene il numero 7.

def is_magic_number(num: int) -> bool:
  number_str= str(num)
  for i in number_str:
    if "7" in number_str:
        return True
  else:
    return False
  

print(is_magic_number(70))
print(is_magic_number(123))

# Scrivi una funzione che somma tutti i numeri interi
# di una lista che sono maggiori di un dato
# valore intero definito threshold.

#def sum_above_threshold(numbers: list[int]):
   


#print(sum_above_threshold([15, 5, 25], 20))

# lista =(15, 5, 25)
# x= 20 
# count=[]
# for i in lista:
#    if x < lista[i]:
      
#       lista(min(x))

   

# numbers: list[int] = [1, 2; 3, 4, 5)

# for i in range(numbers):
#     #print('Number:, i)
   
# Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) 
# è soddisfatta per procedere con un'operazione. L'operazione può procedere solo 
# se la condizione A è vera o se entrambe le condizioni B e C sono vere.
# La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" 
# a seconda delle condizioni che sono soddisfatte.

def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    # cancella pass e scrivi il tuo codice
    if conditionA == True or conditionB and conditionC ==True:
       return "Operazione permessa"
    else:
       return  "Operazione negata"
    
    
    
print(check_combination(True, False, True))