# QUESTION 1 

"""

2. Classe Customer:

Attributi:

    customer_id: str - Identificativo del cliente.
    name: str - Nome del cliente.
    rented_movies: list[Movie] - Lista dei film noleggiati.

Metodi:

    rent_movie(movie: Movie): Aggiunge il film nella lista rented_movies 
    se non è già stato noleggiato, altrimenti stampa il messaggio 
    "Il film {movie.title} è già noleggiato."
    return_movie(movie: Movie): Rimuove il film dalla
      lista rented_movies se già presente, altrimenti
        stampa il messaggio "Il film {movie.title} non è
          stato noleggiato da questo cliente."

3. Classe VideoRentalStore:

Attributi:

    movies: dict[str, Movie] - Dizionario che ha per chiave l'id del film e per valore l'oggetto Movie.
    customers: dict[str, Customer] - Dizionario che ha per chiave l'id del cliente e per valore l'oggetto Customer.

Metodi:

    add_movie(movie_id: str, title: str, director: str): Aggiunge un nuovo film nel videonoleggio se non è già presente, altrimenti stampa il messaggio "Il film con ID {movie_id} esiste già."
    register_customer(customer_id: str, name: str): Iscrive un nuovo cliente nel videonoleggio se non è già presente, altrimenti stampa il messaggio "Il cliente con ID {customer_id} è già registrato."
    rent_movie(customer_id: str, movie_id: str): Permette al cliente di noleggiare un film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio "Cliente o film non trovato."
    return_movie(customer_id: str, movie_id: str): Permette al cliente di restituire un film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio "Cliente o film non trovato."
    get_rented_movies(customer_id: str): list[Movie] - Restituisce la lista dei film noleggiati dal client (customer.rented_movies) se il cliente esiste nel videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una lista vuota.

"""

class Movie:

    def __init__(self, movie_id: str,
                        title: str,
                        director: str,
                        is_rented: bool) -> None:
        
        self.movie_id= movie_id
        self.title= title
        self.director = director
        self.is_rented = is_rented
    

    def rent(self):
        if self.is_rented ==False:
            self.is_rented == True
            return f"Il film {self.title} è già noleggiato."


    def return_movie(self):
        if self.is_rented ==False:
            self.is_rented == True
            return f"Il film {self.title} non è attualmente noleggiato"
    
class Customer:
    def __init__(self, 
    customer_id: str,
    name: str,
    rented_movies: list[Movie]) -> None:
        
        self.customer_id= customer_id
        self.name= name
        self.rented_movies = list[Movie]


    def  rent_movie(self,movie: Movie):
        
        """ Aggiunge il film nella lista rented_movies 
            se non è già stato noleggiato, altrimenti 
            stampa il messaggio Il film {movie.title}
            è già noleggiato."""
        
        if movie.is_rented== False:
             self.rented_movies.append(movie)
        else:
            return f'Il film {movie.title} è già noleggiato'


class VideoRentalStore:
    pass


# Creazione di un nuovo videonoleggio
videonoleggio = VideoRentalStore()

# Aggiunta di nuovi film
videonoleggio.add_movie("1", "Inception", "Christopher Nolan")
videonoleggio.add_movie("2", "The Matrix", "Wachowski Brothers")

# Registrazione di nuovi clienti
videonoleggio.register_customer("101", "Alice")
videonoleggio.register_customer("102", "Bob")

# Noleggio di film
videonoleggio.rent_movie("101", "1")
videonoleggio.rent_movie("102", "2")

# Tentativo di noleggiare un film già noleggiato
videonoleggio.rent_movie("101", "1")

# Restituzione di film
videonoleggio.return_movie("101", "1")

# Tentativo di restituire un film non noleggiato
videonoleggio.return_movie("101", "1")

# Ottenere la lista dei film noleggiati da un cliente
rented_movies_alice = videonoleggio.get_rented_movies("101")
print(f"Film noleggiati da Alice: {[movie.title for movie in rented_movies_alice]}")

rented_movies_bob = videonoleggio.get_rented_movies("102")
print(f"Film noleggiati da Bob: {[movie.title for movie in rented_movies_bob]}")


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
        return None
    
print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))
print(trova_chiave_per_valore({'k1': 'v1', 'k2': 'v2'}, 'v3'))


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


class Account:
    
    def __init__(self,account_id: str, balance:float=0 ) -> None:
         
        self.account_id = account_id
        self.balance = balance
    
    def deposit(self,amount: int):
         self.balance += amount 

    def get_balance(self):
         return self.balance
         
class Bank:

    def __init__(self) -> None:
        self.accounts:dict = {}

    def create_account(self,account_id: str): 
        self.account = Account(account_id,0)
        if account_id not in self.accounts:
            self.accounts[account_id] = self.account
            return self.account
        else:
            raise ValueError("Account with this ID already exists")


    def deposit(self,account_id, amount: float): 
        if account_id in self.accounts:
            self.account.balance += amount
        else:
            raise ValueError(f"Account not found")


          
    def get_balance(self,account_id): 
        if account_id in self.accounts:
            return self.account.balance
        else:
    
            raise ValueError(f"Account not found")



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

# QUESTION 5

"""
1. Classe Base: Veicolo
Crea una classe base chiamata Veicolo
con i seguenti attributi e metodi:
 
Attributi:
- marca (stringa)
- modello (stringa)
- anno (intero)

Metodi:
- __init__(self, marca, modello, anno): metodo costruttore
 che inizializza gli attributi marca, modello e anno.
- descrivi_veicolo(self): metodo che stampa una descrizione 
del veicolo nel formato "Marca: [marca], Modello: [modello], Anno: [anno]".

"""

class Veicolo:
    def __init__(self, marca: str, modello: str, anno: int) -> None:
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def descrivi_veicolo(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}')

class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, numero_porte: int) -> None:
        super().__init__(marca, modello, anno)

        self.numero_porte= numero_porte

    def descrivi_veicolo(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}')

class Moto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, tipo:str) -> None:
        super().__init__(marca, modello, anno)
        self.tipo = tipo

    def descrivi_veicolo(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}')

# QUESTION6
"""
Scrivi una funzione che unisce due dizionari. 
Se una chiave è presente in entrambi, somma i loro valori.
"""
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    newdict:dict = {}
   
    for key1, value1 in dict1.items():
        for key2, value2 in dict2.items():
            if key1 == key2:
                newdict[key1]= value1 + value2
                return newdict
     


print(merge_dictionaries({'x': 5}, {'x': -5})) # {'x': 0}\
print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(merge_dictionaries({'a': 3}, {'b': 4}))
print(merge_dictionaries({}, {}))

# QUESTION 7
"""
Scrivi una funzione che accetti tre parametri: 
username, password e status di attivazione dell'account 
(attivo/non attivo). L'accesso è consentito solo
se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo.
La funzione ritorna "Accesso consentito" oppure "Accesso negato".
"""
def check_access(username: str, password:str, is_active: bool) -> str:
    # cancella ... è definisci il tipo di dato per password, successivamente 
    # cancella pass e scrivi il tuo codice
    if is_active == True and username == "admin" and password == "12345":
        return "Accesso consentito"
    elif is_active == True and username == "admin" and password != "12345":
        return "Accesso negato"
    elif is_active == True and username != "admin" and password == "12345":
        return "Accesso negato"
    elif is_active == True and username != "admin" and password != "12345":
        return "Accesso negato"
    elif is_active== False:
        return "Accesso negato"

    
print(check_access("admin", "12345", True))
print(check_access("admin", "54321", True))



# QUESTION 11
"""
Scrivi una funzione che prende una lista di numeri e ritorna un 
dizionario che classifica i numeri in liste separate 
per numeri pari e dispari.
"""

def classifica_numeri(lista: int) -> dict[str:list[int]]:
    newdict: dict = {}
    newdict['pari']= []
    newdict['dispari']=[]
    for elements in lista:
        if elements % 2 == 0:
            newdict["pari"].append(elements)
        elif elements % 2 != 0:
            newdict["dispari"].append(elements)

    return newdict


print(classifica_numeri([1, 2, 3, 4, 5, 6]))
print(classifica_numeri([]))


# QUESTION 12
"""
Scrivi una funzione che, data una lista,
ritorni un dictionary che mappa ogni elemento
alla sua frequenza nella lista.
"""
def frequency_dict(elements: list) -> dict:

    newdict: dict = dict()
    for item in elements:
        if item in newdict:
            newdict[item] += 1
        else:
            newdict[item]= 1

print(frequency_dict(['mela', 'banana', 'mela']))


# QUESTION 13

"""
Scrivi una funzione che somma tutti i numeri interi
di una lista che sono maggiori di un dato valore 
intero definito threshold.
"""
def sum_above_threshold(numbers: list[int], n: int) -> int:

    l:list=[]
    for i in numbers:
        if i > n:
            l.append(i)        
    return sum(l)
    
print(sum_above_threshold([15, 5, 25], 20))

#QUESTION 14
"""
Scrivi una funzione che accetti un dizionario di prodotti
con i prezzi e restituisca un nuovo dizionario con
solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
"""
def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    d: dict={}
    for key, value  in prodotti.items():
        if value > 20:
            sconto= (value * 10 /100)
            d[key]= value - sconto
    return d
  
print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))

# QUESTION 15

"""
Scrivi una funzione che converta una lista di tuple 
(chiave, valore) in un dizionario. Se la chiave è già presente, 
aggiungi il valore alla lista di valori già associata alla chiave."""

def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    d:dict ={}
    for i in tuples:
        if i[0] not in d:
            d[i[0]]=[i[1]]
        else:
            d[i[0]]+=[i[1]]
    return d
            



print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)])) #{'a': [1, 3], 'b': [2]}

print(lista_a_dizionario([]))


