"""" n un file chiamato "film.py", si definisca la classe Film che rappresenta un film preso a nolleggio. 
In tale classe, definire un codice identificativo (int) ed un titolo (string). 
Entrambi gli attributi sono da considerarsi privati.
 
- Definire i seguenti metodi:

    init(id, title): metodo costruttore.
    setID(id): che consente di impostare il codice identificativo del film, 
    modificando il valore del relativo attributo.
    setTitle(title): che consente di impostare il codice identificativo
    del film, modificando il valore del relativo attributo.
    getID(): che consente di ritornare il valore del codice identificativo di un film.
    getTitle(): che consente di ritornare il valore del titolo di un film.
    isEqual(otherFilm): che ritorna true se il codice identificativo di due film è uguale."""


class Film:
    def __init__(self, id:int, title:str ) :
        self.__id = id 
        self.__title= title

    def setID(self,id:int)-> None: 
        self.__id = id

    def setTitle(self,title: str)-> None:
        self.__title =title

    def getID(self):
        return self.__id
    
    def getTitle(self) :
        return self.__title
    
    def isEqual(self ,otherFilm) -> bool:
        if otherFilm == self.getID():
        #if self.getID() == otherFilm.getID():
            print(True)
            return True
        else:
            print(False)
            return False
        
    def __str__(self) -> str:
        return f'ID = {self.__id} Title = {self.__title}'
        

film1: Film= Film(222,"ma")
film2: Film= Film(111,"Balla coi lupi ")


film1.setID(111)
film1.setTitle("l'ultimo dei moicani")


print(film1.getTitle())

print(film1)

film1.isEqual(111)
film1.isEqual(131)


