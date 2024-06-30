from film import Film
from movie_genre import Azione,Commedia,Drama


class Noleggio():
    def __init__(self,film_list:list) -> None:
        self.film_list=[]

        self.rented_film: dict={}

    def AddFilm (self,film:Film)-> None:
        if film is not self.film_list:
            self.film_list.append(film)
        else: 
            film is self.film_list
            print(f'il film è gia presente nella lista {film.getTitle()}')
        
    def isAvaible(self,film:Film) -> bool:
        if film is self.film_list:
            print(f'Il film scelto è disponibile: {film.getTitle()}".')
            return True
        else: 
            print(f'Il film scelto non è disponibile: {film.getTitle()}".')
            return False
        
    
        
film1: Film= Film(222,"ma")

film1.setID(111)
film1.setTitle("l'ultimo dei moicani")


print(film1.getTitle())

print(film1)

film1.isEqual(111)
film1.isEqual(131)
lista_noleggio=[]
noleggio1:Noleggio = Noleggio(lista_noleggio)

noleggio1.AddFilm(film1)
noleggio1.AddFilm(film2)

noleggio1.isAvaible(film1)

