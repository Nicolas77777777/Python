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

lista: list =([15, 5, 25], 20)
for i in lista:
   print(i)
