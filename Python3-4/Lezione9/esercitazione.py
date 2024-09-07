# QUESTION 1
# QUESTION 2
"""
Data una stringa s e una lista di stringhe 
wordDict, restituisce True se s può essere 
segmentato in una sequenza separata da spazi
di una o più parole del dizionario; False altrimenti.

Tieni presente che la stessa parola 
nel dizionario può essere riutilizzata
 più volte nella segmentazione.
"""
def word_break(s: str, wordDict: list[str]) -> bool:

    for p in wordDict:
        s= s.replace(p,'')
    
    if s =='':
            return True
    else: 
            return False
        
    
        

print(word_break("leetcode",["leet","code"]))
print(word_break("applepenapple", ["apple","pen"]))
print(word_break("catsandog",["cats","dog","sand","and","cat"]))


# QUESTION 3
# QUESTION 4
# QUESTION 5
# QUESTION 6
# QUESTION 7
# QUESTION 8
# QUESTION 9
# QUESTION 10

"""" 
Date due stringhe s e t, restituire True
se t è un anagramma di s, e False altrimenti.

Un anagramma è una parola o una frase formata 
riorganizzando le lettere di una parola o
 frase diversa, in genere utilizzando tutte
 le lettere originali esattamente una volta"""

def anagram(s: str, t: str) -> bool:
    s.lower()
    t.lower()

    if sorted(s) == sorted(t):
         
         return True
    
    else: 
         
         return False


print(anagram("anagram","nagaram"))

# QUESTION 6
"""" Progettare un semplice sistema bancario con i seguenti requisiti:

    Classe del Account:
        Attributi:
            account_id: str - identificatore univoco per l'account.
            balance: float - il saldo attuale del conto.
        Metodi:
            deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
            get_balance(): restituisce il saldo corrente del conto.
    Classe Bank:
        Attributi:
            accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
        Metodi:
            create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
            deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
            get_balance(account_id): restituisce il saldo del conto con l'ID specificato."""


class Account:
    
    def __init__(self,account_id: str, balance:float=0 ) -> None:
         
        self.account_id = account_id
        self.balance = balance
    
    def deposit(self,amount: int):
         self.balance += amount 

    def get_balance(self):
         return self.balance
         

class Bank:

    def __init__(self, accounts: dict[str, Account],) -> None:
            self.accounts= accounts

    def create_account(self,account_id: str): # crea un nuovo account con l'ID specificato e un saldo pari a 0.
         account_id = account_id

    def deposit(self,account_id, amount: float): # deposita l'importo specificato sul conto con l'ID fornito.
          #if account_id :
               
            pass
            
    def get_balance(self,account_id): # restituisce il saldo del conto con l'ID specificato."""
         pass

account1= 

bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())



bank = Bank()
account1 = bank.create_account("123")
bank.deposit("123",100)
print(bank.get_balance("123"))

bank = Bank()
account2 = bank.create_account("456")
bank.deposit("456",200)
print(bank.get_balance("456"))