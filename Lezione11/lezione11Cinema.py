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

    def lista_film (self):
        film_dispo:list=[]
        

class Sala:

    def __init__(self,id_sala : int ) -> None:

        self.id_sala = id_sala
        self.tot_posti: int = 100
    

    def prenota_posti(self,num_posti: int):

        if num_posti <= self.tot_posti:
            return num_posti 
        else:
            return f'non è possibile prenotare un numero di posti maggiori a {self.tot_posti}'
            

    def posti_disponibili(self):
          return self.prenota_posti() - self.tot_posti
    
    def film_disponibili(self, titolo_film:Film):
        for i in Film:
            return i[titolo_film.titolo]




class Cinema:
    def __init__(self, sale:list) -> None:
        self.sale= sale
        
    def aggiungi_sala(self, sala: str):
        self.sale.append(sala)

    def prenota_film(self,titolo_film , num_posti):
        pass
        
        

        


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

lista_film= Sala(film_dispo=[])
cinema_1.sale



