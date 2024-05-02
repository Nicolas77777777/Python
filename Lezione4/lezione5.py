# set insieme

# Scrivi una funzione che, dato un numero intero,
# determina se è un "numero magico".
# Un numero magico è definito come un 
# numero che contiene il numero 7.

def is_magic_number(num: int) -> bool:
  number_str= str(num)
  for i in range(len(number_str)):
    if number_str[i] == 7:
        return True
  else:
    return False
  
    

print(is_magic_number(70))


#print(is_magic_number(123)
