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
    def __init__(self, titolo: str, durata: float) -> None:
        self.titolo = titolo
        self.durata = durata

    def lista_film(self, film_dispo: list) -> list:
        film_dispo.append(self.titolo)
        return film_dispo


class Sala:
    def __init__(self, id_sala: int, film: Film = None) -> None:
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
    def __init__(self) -> None:
        self.sale: list = []

    def aggiungi_sala(self, sala: Sala):
        self.sale.append(sala)

    def prenota_film(self, titolo_film: str, num_posti: int) -> str:
        for sala in self.sale:
            if sala.film and sala.film.titolo == titolo_film:
                return sala.prenota_posti(num_posti)
        return "Film non trovato nelle sale."


# Definizione dei film
film_1 = Film("Balla coi Lupi", 90)
film_2 = Film("Senza Esclusioni di Colpi", 120)
film_3 = Film("Il Gladiatore", 130)

# Definizione delle sale e impostazione dei film
sala_1 = Sala(1, film_1)
sala_2 = Sala(2, film_2)
sala_3 = Sala(3, film_3)

# Creazione del cinema e aggiunta delle sale
cinema_1 = Cinema()
cinema_1.aggiungi_sala(sala_1)
cinema_1.aggiungi_sala(sala_2)
cinema_1.aggiungi_sala(sala_3)

# Creazione della lista dei film disponibili
film_disponibili: list = []
film_1.lista_film(film_disponibili)
film_2.lista_film(film_disponibili)
film_3.lista_film(film_disponibili)
print(film_disponibili)

# Prenotazione dei posti
print(cinema_1.prenota_film("Il Gladiatore", 30))
print(cinema_1.prenota_film("Il Gladiatore", 80))  
print(cinema_1.prenota_film("Film Non Disponibile", 30))


""" Scrivi un programma in Python che gestisca un magazzino. 
Il programma deve permettere di aggiungere prodotti al magazzino, 
cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
Test case:

    Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. 
    Successivamente, aggiunge i prodotti al magazzino.
    Il sistema cerca un prodotto per verificare se esiste nell'inventario.
    Il sistema verifica la disponibilità dei prodotti in inventario."""


class Prodotto: 
    def __init__(self, nome : str, quantita : int ) -> None:

        self.nome= nome
        self.quantita = quantita

    def dizionario (self):
        prodotto: dict = dict
        prodotto = {
                    self.nome : self.quantita
                        }
        return prodotto
        

class Magazzino:

    def aggiungi_prodotto(prodotto: Prodotto):
        pass


    def cerca_prodotto(nome: str):
        pass


    def verifica_disponibilità(nome: str):
        pass


scarpe = Prodotto("scarpe",10)
camicia = Prodotto("camica",10)

Prodotto.dizionario(self=scarpe)
divmod






