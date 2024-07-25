

class Book:
    def __init__(self,book_id: str, title_id: str, author: str) -> None:
        pass
    
        self.book_id: str = book_id
        self.title_id: str = title_id
        self.author: str = author
        self.is_borrowed = False

    def borrow(self) -> None:
        """Contrassegna il libro come preso in prestito se non è già preso in prestito."""
        self.is_borrowed = True
    
    def return_book(self) -> None:
        """ Contrassegna il libro come restituito."""
        self.is_borrowed = False


class Member:

    def __init__(self,member_id: str, name: str) -> None:
            
        self.member_id: str = member_id
        self.name: str = name
        self.borrowed_books: list[Book] = []
    
    def borrow_book(self,book:Book):
         
        """
        aggiunge il libro nella 
        lista borrowed_books se
        non è già stato preso in prestito."""

        if not book.is_borrowed:
         
            self.borrowed_books.append(book)

        return self.borrowed_books
             
             
             
    def return_book(self,book):
        """ rimuove il libro dalla lista borrowed_books."""
        pass

class Library:

    def __init__(self) -> None:

        self.books: dict[str, Book] = {}# dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
        self.members: dict[str, Member]= {} #dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
   
    def add_book(book_id: str, title: str, author: str): #Aggiunge un nuovo libro nella biblioteca.
        pass
    def register_member(member_id:str, name: str): #Iscrive un nuovo membro nella biblioteca.
        pass
    def borrow_book(member_id: str, book_id: str): #Permette al membro di prendere in prestito il libro.
        pass
    def return_book(member_id: str, book_id: str):#Permette al membro di restituire il libro.
        pass
    def get_borrowed_books(member_id): 
        
        # list[Book]:restituisce la lista dei libri presi in prestito dal membro
        pass


book1:Book = Book("123","franco","pippo")


print(book1.borrow())
print(book1.return_book())

membro1: Member = Member("Id..1","pietro")


print(membro1.borrow_book(book1))




