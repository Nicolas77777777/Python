def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA == True or conditionB== True or conditionC == True :
        return "Operazione permessa"
    else:
         return "Operazione negata"
    
#QUESTION 3
"""
Scrivi una funzione che prenda un dizionario e un valore,
e ritorni la prima chiave che corrisponde a quel valore,
 o None se il valore non è presente.
"""

def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    for key, value in dizionario.items():
        if value == valore:
            return key
    else:
        return False
    
print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))


#QUESTION 4
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


# class Account:
    
#     def __init__(self,account_id: str, balance:float=0 ) -> None:
         
#         self.account_id = account_id
#         self.balance = balance
    
#     def deposit(self,amount: int):
#          self.balance += amount 

#     def get_balance(self):
#          return self.balance
         

# class Bank:

#     def __init__(self, accounts: dict[str, Account]) -> None:
#             self.accounts= accounts

#     def create_account(self,account_id: str): # crea un nuovo account con l'ID specificato e un saldo pari a 0.
#         self.accounts[account_id] = Account(account_id, 0) 

#     def deposit(self,account_id, amount: float): # deposita l'importo specificato sul conto con l'ID fornito.
#           if account_id in self.accounts:
#                pass
                     
            
                
#     def get_balance(self,account_id): # restituisce il saldo del conto con l'ID specificato."""
#         pass

# account= Account("123")

# #bank1: Bank = Bank("123",account)




# bank = Bank()
# account1 = bank.create_account("123")
# print(account1.get_balance())



# bank = Bank()
# account1 = bank.create_account("123")
# bank.deposit("123",100)
# print(bank.get_balance("123"))

# bank = Bank()
# account2 = bank.create_account("456")
# bank.deposit("456",200)
# print(bank.get_balance("456"))