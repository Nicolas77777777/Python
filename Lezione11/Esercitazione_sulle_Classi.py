""""- Film: Rappresenta un film con titolo e durata.
 
- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

Metodi:
    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
- Cinema: Gestisce le operazioni legate alla gestione delle sale.

Metodi:
    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta
      di prenotare posti. Restituisce un messaggio di stato.

Test case:

    Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
    Un cliente sceglie un film e prenota un certo numero di posti.
    Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione."""

class Film:

    def __init__(self, titolo : str, durata : float) -> None:

        self.titolo = titolo
        self.durata = durata

    def lista_film (self, film_dispo: list) ->list:
        film_dispo.append(self.titolo)
        return film_dispo

class Sala:

    def __init__(self,id_sala : int, film:Film = None) -> None:

        self.id_sala = id_sala
        self.tot_posti: int = 100
        self.posti_prenotati = 0
        self.film = film 

    
    def prenota_posti(self, num_posti: int) -> str:
        if self.posti_disponibili() >= num_posti:
            self.posti_prenotati += num_posti
            return f"Prenotazione di {num_posti} posti confermata per il film '{self.film.titolo}'."
        else:
            return f"Non ci sono abbastanza posti disponibili. Posti disponibili: {self.posti_disponibili()}."

    def posti_disponibili(self) -> int:
        return self.tot_posti - self.posti_prenotati

    def imposta_film(self, film: Film) -> None:
        self.film = film

class Cinema:
    def __init__(self, sale:list) -> None:
        self.sale = sale
        
    def aggiungi_sala(self, sala:Sala):
        self.sale.append(sala)

    def prenota_film(self, titolo_film:str , num_posti: int):
        for sala in self.sale:
            if sala.film and sala.film.titolo == titolo_film:
                return sala.prenota_posti(num_posti)
            else:
                return "film non presente nelle sale. "

        
                


film_1 = Film("Balla coi Lupi",90)
film_2 = Film("Senza Esclusioni di Colpi", 120)
film_3 = Film("Il Gladiatore", 130)

sala_1 = Sala(1)  
sala_2 = Sala(2)  
sala_3 = Sala(3)  

cinema_1= Cinema(sale=[])
cinema_1.aggiungi_sala(sala_2.id_sala)
cinema_1.aggiungi_sala(sala_1.id_sala)
cinema_1.aggiungi_sala(sala_3.id_sala)

film_disponibili: list = []
film_1.lista_film(film_disponibili)
film_2.lista_film(film_disponibili)
film_3.lista_film(film_disponibili)
print(film_disponibili)

print(cinema_1.prenota_film("Il Gladiatore",30))









