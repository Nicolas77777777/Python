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

#bank = Bank()
#account1 = bank.create_account("123")
#print(account1.get_balance())

# class Account:
    
#     def __init__(self,account_id: str, balance:float=0 ) -> None:

#         self.account_id = account_id
#         self.balance: float = balance

#     def deposit(self,amount: float):  
#         amount +=  self.balance
        
    
#     def get_balance(self):
#         return self.balance

# class Bank:

#     def __init__(self, accounts: dict[str, Account],) -> None:
#             self.accounts= accounts

#     def create_account(self, account_id:Account ):
#         account_id = account_id
        

#     def deposit(self,account_id, amount):
#         pass

#     def get_balance(self, account_id:Account):
#         account_id = account_id.get_balance

    
# bank= Bank()
# account1= Bank.create_account("123")

# print(())



class Member:
    pass

class Book:
    def __init__(self, book_id: str) -> None:
        pass
    

class Library:
    pass
