import unittest
from unittest import TestCase
from film import Film
from movie_genre import Azione, Drama, Commedia
from noleggio import Noleggio



""" Testare il Noleggio di un Film (rentAMovie):
- Scrivere un test per verificare che un film disponibile possa essere noleggiato correttamente.
- Dopo il noleggio, verificare che il film non sia più disponibile.
- Verificare che il film noleggiato appaia nella lista dei film noleggiati dal cliente.



Testare la Restituzione di un Film (giveBack):
- Noleggiare un film e poi restituirlo.
- Verificare che il film restituito sia nuovamente disponibile.
- Verificare che il film restituito non sia più nella lista dei film noleggiati dal cliente.

Testare il Calcolo della Penale di Ritardo (calcolaPenaleRitardo):
- Scrivere test per verificare il calcolo della penale di ritardo per film di diversi generi (azione, commedia, dramma).

Testare la Stampa dei Film Disponibili (printMovies):
- Verificare che la lista dei film disponibili contenga i titoli corretti.

Testare la Stampa dei Film Noleggiati da un Cliente (printRentMovies):
- Noleggiare uno o più film per un cliente.
- Verificare che la stampa dei film noleggiati contenga i titoli corretti."""


class TestFilm (TestCase):

    def setUp(self) -> None:

        self.film1 = Commedia(1, "The Shawshank Redemption")
        self.film2 = Azione(2, "The Godfather")
        self.film3 = Azione(3, "The Dark Knight")
        self.film4 = Azione(4, "Pulp Fiction")
        self.film5 = Drama(5, "Schindler's List")        
        self.film6=  Azione(6,"L'ultimo dei Moicani")
        self.film7=  Azione(7,"Balla coi lupi")
        self.film8 = Commedia(8,"Mamma ho perso l'aereo")
        self.film9 = Commedia(9,"Pallotola spuntata")
        self.film10 = Commedia(10, "La banda del gobbo")

        self.lista_Blokbuster = [self.film1, self.film2, self.film3,
                            self.film4, self.film5, self.film6,
                             self.film7, self.film8, self.film9,
                             self.film10     ]

        self.blockbuster:Noleggio= Noleggio(self.lista_Blokbuster)


    def test_IsAvaible(self):
        #  test per verificare che un film disponibile ritorni True.
        message: str = f'Error: i film scelto non è disponibile '
        self.assertTrue(self.blockbuster.isAvaible(self.film1),message)
        self.assertFalse(self.blockbuster.isAvaible(Azione(333,"Rocky")),message)

    def test_rent_a_movie(self):
        self.blockbuster.rentAMovie(self.film2,44)
        self.assertFalse(self.blockbuster.isAvaible(self.film2))
        self.assertIn(self.film2, self.blockbuster.rented_film[44])



    def test_rent_a_movie_unavailable(self):
        self.blockbuster.rentAMovie(self.film5,111)
        self.blockbuster.rentAMovie(self.film5,222)
        self.assertIn(self.film5, self.blockbuster.rented_film[111])
        self.assertNotIn(self.film2, self.blockbuster.rented_film.get(222,[]),"errore")


    def test_give_back(self):
        self.blockbuster.rentAMovie(self.film5,111)
        self.blockbuster.giveBack(self.film5,11,2)
        self.assertTrue(self.blockbuster.isAvaible(self.film5))
        self.assertNotIn(self.film5,self.blockbuster.rented_film.get)(111,[])

     
    def test_calcola_penale_ritardo(self):

        self.assertEqual(self.film2.calcolaPenaleRitardo(4),12.00,"è GIUSTO  ")

    


    

if __name__ == "__main__":

    unittest.main()




