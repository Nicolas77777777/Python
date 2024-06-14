
"""Vogliamo gestire un contatore che può essere incrementato,
 decrementato, resettato e visualizzato. La classe offre
un modo semplice per tenere traccia di un conteggio 
che non può diventare negativo.

Classe Contatore
Attributi:
- conteggio: un intero che conserva il valore del conteggio, inizializzato a 0.

Metodi:
- __init__(): Inizializza l'attributo conteggio a 0.
- setZero(): Imposta il conteggio a 0.
- add1(): Incrementa il conteggio di 1.
- sub1(): Decrementa il conteggio di 1, ma non permette che il conteggio diventi negativo.
 Se il conteggio è già 0, stampa un messaggio di errore.
- get(): Restituisce il valore corrente del conteggio.
- mostra(): Stampa a schermo il valore corrente del conteggio."""

class Contatore:
    def __init__(self):
        self.conteggio = 0
    
    def setZero(self):
        self.conteggio = 0
    
    def add1(self):
        self.conteggio += 1
    
    def sub1(self):
        if self.conteggio > 0:
            self.conteggio -= 1
        else:
            print("Non è possibile eseguire la sottrazione")
    
    def get(self):
        return self.conteggio
    
    def mostra(self):
        print(f"Conteggio attuale: {self.conteggio}")

# Esempio di utilizzo della classe
contatore = Contatore()
contatore.mostra()  # Output: Il valore corrente del conteggio è: 0
contatore.add1()
contatore.add1()

contatore.add1()

contatore.mostra()  # Output: Il valore corrente del conteggio è: 1
contatore.sub1()
contatore.mostra()  # Output: Il valore corrente del conteggio è: 0
contatore.sub1()    # Output: Errore: il conteggio è già 0 e non può essere decrementato.

class Veicolo:
    def __init__(self, marca: str, modello: str, anno: int ) :
        self.marca = marca
        self.modello= modello 
        self.anno = anno

    def descrivi_veicolo(self):
        descrivi = f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}'
        return descrivi 

class Auto(Veicolo):

    def __init__(self, marca: str, modello: str, anno: int, numero_porte: int):
        super().__init__(marca, modello, anno)

        self.numero_porte = numero_porte


    def descrivi_veicolo(self):
        descrivi = f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}'
        return descrivi 
    
class Moto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, tipo: str):
            super().__init__(marca, modello, anno)

            self.tipo= tipo 

    def descrivi_veicolo(self):
        descrivi = f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}'
        return descrivi 
    

veicolo = Veicolo("Generic", "Model", 2020)
auto = Auto("Toyota", "Corolla", 2021, 4)
moto = Moto("Yamaha", "R1", 2022, "sportiva")

veicolo.descrivi_veicolo()
auto.descrivi_veicolo()
moto.descrivi_veicolo()


class RecipeManager:
    def __init__(self) -> dict:
        self.recipes: dict = {}

    def create_recipe(self, name: str, ingredients:str) -> dict:
        self.recipes[name]= ingredients
        return self.recipes


    def add_ingredient(self, recipe_name: str, ingredient: str):
        recipe_name:dict = recipe_name
        if recipe_name == self.recipes.keys():
            pass

     

    def remove_ingredient(self, recipe_name, ingredient):
        pass
   

    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
       pass

manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
