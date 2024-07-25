class Movie:

    def __init__(self, movie_id: str, title: str, director: str, is_rented: bool) -> None:
        
        self.movie_id= movie_id
        self.title= title
        self.director = director
        self.is_rented = is_rented
    

    def rent(self):
        """ Contrassegna il film come noleggiato se non è già noleggiato. Se il film non è già noleggiato
        imposta is_rented a True, 
        altrimenti stampa il messaggio
        "Il film {self.title} è già noleggiato."""
        
        if not self.is_rented:
            self.is_rented == True  
        else:
            return f"Il film {self.title} è già noleggiato."


    def return_movie(self):
        if self.is_rented :
            self.is_rented == False
        else:
            return f"Il film {self.title} non è attualmente noleggiato"
    
class Customer:
    def __init__(self, customer_id: str, name: str, rented_movies: list[Movie]) -> None:
        
        self.customer_id= customer_id
        self.name= name
        self.rented_movies = rented_movies


    def  rent_movie(self,movie: Movie):
        
        """ Aggiunge il film nella lista rented_movies 
            se non è già stato noleggiato, altrimenti 
            stampa il messaggio Il film {movie.title}
            è già noleggiato."""
        
        if movie.is_rented== False:
             self.rented_movies.append(movie)
        else:
            return f'Il film {movie.title} è già noleggiato'


    def return_movie(self,movie: Movie):
        """
        Rimuove il film
        dalla lista rented_movies se già presente,
        altrimenti stampa il messaggio "Il film {movie.title} 
        non è stato noleggiato da questo cliente."
        """
        if movie not in self.rented_movies:
            return f'Il film {movie.title} non è stato noleggiato da questo cliente."'
        else:
            self.rented_movies.remove(movie)


class VideoRentalStore:
    def __init__(self) -> None:
        self.movies: dict[str, Movie]= {}
        self.customers: dict[str, Customer]={}

    """
      Attributi:
    movies: dict[str, Movie] - Dizionario 
     che ha per chiave l'id del film e per valore l'oggetto Movie.
     customers: dict[str, Customer]
    Dizionario che ha per chiave l'id del 
     cliente e per valore l'oggetto Customer. 
    """
    pass


    def add_movie(movie_id: str, title: str, director: str):
        """ Aggiunge un nuovo film nel videonoleggio se 
        non è già presente, altrimenti stampa il messaggio 
        "Il film con ID {movie_id} esiste già."""


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