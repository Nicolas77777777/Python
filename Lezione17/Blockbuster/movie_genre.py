from film import Film


class Azione(Film):
    def __init__(self, id: int, title: str):
        super().__init__(id, title)
        self.__genere:str  = "Azione"
        self.__penale: float = 3.00
    
    def getGenere(self) :
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self,giorni_ritardo:int):
        penale_ritardo:float= self.__penale * giorni_ritardo
        return penale_ritardo
    
class Commedia(Film):
    def __init__(self, id: int, title: str):
        super().__init__(id, title)
        self.__genere:str  = "Commedia"
        self.__penale: float = 2.50
    
    def getGenere(self):
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self,giorni_ritardo:int):
        penale_ritardo:float= self.__penale * giorni_ritardo
        return penale_ritardo
    

class Drama(Film):
    def __init__(self, id: int, title: str):
        super().__init__(id, title)
        self.__genere:str  = "Drama"
        self.__penale: float = 2.00
    
    def getGenere(self):
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self,giorni_ritardo:int):
        penale_ritardo:float= self.__penale * giorni_ritardo
        return penale_ritardo


# azi1:Azione= Azione(111,"Braveheart")
# print(azi1.getGenere(), azi1.getPenale())

# print(azi1.calcolaPenaleRitardo(3))