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



class Cinema:
    def __init__(self, sale:list) -> None:
        self.sale= sale
        
    def aggiungi_sala(self, sala: str):
        self.sale.append(sala)
        
        

        


new_film = Film("Balla coi Lupi",90)

sala_1 = Sala(1)  

print(new_film.titolo, new_film.durata)

print(sala_1.id_sala)

cinema_1= Cinema(sale=[])

print(cinema_1.aggiungi_sala(sala_1.id_sala))
