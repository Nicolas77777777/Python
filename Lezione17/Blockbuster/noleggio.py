from film import Film
from movie_genre import Azione,Commedia,Drama


class Noleggio():
    def __init__(self,film_list:list) -> None:
        self.film_list=[]
        self.rented_film: dict={}
        self.__clientID= None

    def AddFilm (self,film:Film)-> None: # appende i film alla lista dei film disponibile in  videoteca
        if film in self.film_list:
            print(f'il film è gia presente nella lista {film.getTitle()}')
        else: 
            film  not in self.film_list
            self.film_list.append(film)
    
    def RemoveFilm (self,film:Film) -> None:
        self.film_list.remove(film)
                
    def isAvaible(self,film:Film) -> bool:
        if film in self.film_list:
            print(f'Il film scelto è disponibile: {film.getTitle()}".')
            return True
        else: 
            print(f'Il film scelto non è disponibile: {film.getTitle()}".')
            return False
        
    def SetIdClient(self, id_client: int) -> None:
        id_client = self.__clientID

    def GetIdClient(self) -> int:
        return self.__clientID
    
    def rentAMovie(self, film: Film, clientID: int )-> dict:
        cliente: dict = {}
    
        if self.isAvaible(film) == True:
            self.RemoveFilm(film)
            cliente = {"clientID": "film.getTitle()"}
                    
            print(cliente)
        return cliente



""" rentAMovie(film, clientID): tale metodo deve gestire il noleggio 
di un film ed ha come argomenti il film da noleggiare ed il codice 
id del cliente che lo noleggia. Affinché sia possibile noleggiare un film,
 un film deve essere disponibile in negozio. Pertanto, il metodo deve verificare
   la disponibilità. Nel caso in cui il film richiesto sia disponibile, rimuoverlo
     dalla lista dei film disponibili in negozio, poi riempire il dizionario rented_film in questo modo:

    la chiave sarà l'id del cliente che noleggia (id_client)
    il corrispondente valore sarà una lista contenente i film noleggiati da quel cliente.

Pertanto, il film noleggiato, una volta rimosso dalla lista dei 
film disponibili in negozio deve essere aggiunto alla lista dei film noleggiati
 dal cliente dato.  Se il cliente ha potuto noleggiare il film richiesto, stampare:
   "Il cliente {clientId} ha noleggiato {titolo_film}!". 
   Se, invece, il film richiesto non è disponibile pe il noleggio,
stampare: Non è possibile nolegiare il film {titolo_film}!"."""



        
    
film1 = Film(1, "The Shawshank Redemption")
film2 = Film(2, "The Godfather")
film3 = Film(3, "The Dark Knight")
film4 = Film(4, "Pulp Fiction")
film5 = Film(5, "Schindler's List")        
film6: Film= Film(6,"L'ultimo dei Moicani")
film7: Film= Film(7,"Balla coi lupi")


lista_noleggio=[]
noleggio1:Noleggio = Noleggio(lista_noleggio)

noleggio1.AddFilm(film1)
noleggio1.AddFilm(film2)
noleggio1.AddFilm(film3)


noleggio1.isAvaible(film1)
noleggio1.AddFilm(film1)

noleggio1.rentAMovie(film1,111)

