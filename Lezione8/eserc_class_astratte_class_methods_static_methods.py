from abc import ABC, abstractmethod

"""" Create an abstract class Shape with an abstract method area 
and another abstract method perimeter. Then, create two subclasses
 Circle and Rectangle that implement the area and perimeter methods."""

class Shape(ABC):
    def __init__(self, name : str) -> None:
        super().__init__()

        self.name = name

@abstractmethod
def area (self):
    pass

@abstractmethod
def perimeter (self):
    pass

class Circle(Shape):

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def area (self,radius:float):
        area= 3.14 *(radius**2)
        return f'circle area = {area}'
    
    def perimeter (self,radius: float):
        perimeter= (2*3.14)*radius
        return f'circle perimeter = {perimeter}'
    
class Rectangle(Shape):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def area (self, base: float, height:float):
        area= base * height
        return f'rectangle area = {area}'
    
    def perimeter (self, base: float, height:float):
        perimeter= (2*base)+ (2*height)
        return f'rectangle perimeter = {perimeter}'
    
   
ce:Circle = Circle("circle")
re: Rectangle = Rectangle("rectangle")

ce.area(5)
ce.perimeter(7)

re.area(20,18)
re.perimeter(5,5)


"""" Exercise 2: Implementing Static Methods

Create a class MathOperations with a static method add 
that takes two numbers and returns their sum, and another 
static method multiply  that takes two numbers and returns their product."""

class MathOperations:
    def __init__(self) :
         pass
         
    @staticmethod
    def add(num_a: float, num_b: float):
            resul = num_a + num_b
            return resul
        

    @staticmethod
    def multiply(num_a: float, num_b: float):
            resul = num_a * num_b
            return resul
  

s = MathOperations.add (11, 22)
f = MathOperations.multiply (3, 2)

""""
Crea una classe Book contenente i seguenti attributi: titolo, autore, isbn
La classe book deve contenere i seguenti metodi:

 Metodo __str__ per restituire una rappresentazione in formato stringa del libro.

 @classmethod from_string(cls, book_str) per creare un'istanza Book da una stringa nel 
 formato "titolo, autore, isbn". Significa che è necessario utilizzare il riferimento 
 alla classe cls per creare un nuovo oggetto della classe Book utilizzando una stringa.

Esempio:

libro = “La Divina Commedia, D. Alighieri, 999000666”
divina_commedia: Libro = Libro.from_string(libro)
Qui divina_commedia deve contenere un'istanza della classe Book with

titolo = La Divina Commedia, autore = D. Alighieri, isbn = 999000666"""

class Book: 
    def __init__(self, title: str , author: str, isbn: int) :
          
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
          return f'titolo = {self.title}, autore = {self.author}, {self.isbn}'
    
    @classmethod
    def from_string(cls, book_str) :
         pass


book1:Book= Book("La Divina Commedia","D. Alighieri",999000666)


print(book1)

class Member: 
     def __init__(self, name: str, member_id:int):
          
          self.name = name 
          self. member_id = member_id
          self.borrowed_books: list =[]
          pass
     
""" Crea una classe Membro con i seguenti attributi: 
nome, membro_id, prestito_libri
La classe membro deve contenere i seguenti metodi:

 prestito_libro(libro) per aggiungere un libro all'elenco prestiti_libri.

 return_book(libro) per rimuovere un libro dall'elenco dei libri_prestati.

 Metodo __str__ per restituire una rappresentazione di stringa del membro.

 @classmethod from_string(cls, member_str) per creare un'istanza Member 
 da una stringa nel formato "name, member_id".

Crea una classe Library con i seguenti attributi: books, members, total_books
 (attributo della classe per tenere traccia del numero totale di libri)

La classe della libreria deve contenere i seguenti metodi:

 add_book(book) per aggiungere un libro alla libreria e incrementare total_books.

 rimuovi_libro(libro) per rimuovere un libro dalla libreria e diminuire total_books.

 Register_member(membro) per aggiungere un membro alla libreria.

 lend_book(libro, membro) per prestare un libro a un membro.
 Dovrebbe verificare se il libro è disponibile e se il membro è registrato.

 Metodo __str__ per restituire una rappresentazione di stringa 
 della biblioteca con l'elenco dei libri e dei membri.

 @classmethod library_statistics(cls) 
 per stampare il numero totale di libri.

Crea uno script e gioca un po' con le classi:
Crea istanze di libri e membri utilizzando metodi di classe.
 Registra membri e aggiungi libri alla biblioteca. 
 Presta libri ai membri e visualizza lo stato della biblioteca
prima e dopo il prestito. """


# creare una istanza da una stringa

# utilizzare split sulla virgola titolo autore e isbn 

# 
