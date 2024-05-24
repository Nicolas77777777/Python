""""Implementa uno stack LIFO (last-in-first-out) utilizzando solo due code.
 Lo stack implementato dovrebbe supportare tutte le funzioni 
 di uno stack normale (push, top, pop e svuota).

Implementa la classe MyStack:

- push(x: int) -> None: spinge l'elemento x in cima allo stack.
- pop() -> None Rimuove l'elemento in cima allo stack e lo restituisce.
- pop() -> None Restituisce l'elemento in cima allo stack.
- vuoto() -> Nessuno Restituisce vero se lo stack è vuoto, falso altrimenti."""

class Queue:
    list=[]


class MyStack:

    def push(x: int):
        Queue.list.append(x)
    
    def pop(self):
        Queue.list.pop()

    def top (self):
        return Queue.list[-1]
    
    def empty (self):
        if Queue.list == []:
            return True
        else:
            return False



prova = MyStack.push(8)
prova = MyStack.push(4)
prova = MyStack.push(6)


print(prova)

print(Queue.list)

MyStack.pop(list)

print(Queue.list)




def merge(nums1, m, nums2, n):
    
    nums1_copy = nums1[:m]
    
    p1, p2 = 0, 0
    
    for i in range(m + n):
        if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
            nums1[i] = nums1_copy[p1]
            p1 += 1
        else:
            nums1[i] = nums2[p2]
            p2 += 1



"""" Data una stringa s composta da lettere minuscole o maiuscole,
 scrivere una funzione che restituisca la lunghezza del palindromo 
 più lungo che può essere costruito con quelle lettere. Le lettere
   fanno distinzione tra maiuscole e minuscole,
 ad esempio "Aa" non è considerato palindromo qui"""

d= 'abccccdd'
print(len(d),'valore di len')
#def longest_palindrome(s: str) -> int:
  #  for i in range(s):
   #     if i 

    
    
#print(longest_palindrome("abccccdd"))
#print(longest_palindrome("Aa"))


""""
Data una stringa contenente solo i caratteri '(', ')', '{', '}', '[' e ']', 
scrivere una funzione per determinare se la stringa di input è valida.

Una stringa di input è valida se: 

     Le parentesi aperte devono essere chiuse con parentesi dello stesso tipo.
     Le parentesi aperte devono essere chiuse nell'ordine corretto.
     Ad ogni parentesi chiusa corrisponde una 
     parentesi aperta dello stesso tipo."""



1






