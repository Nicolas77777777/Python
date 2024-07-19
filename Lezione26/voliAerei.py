from abc import ABC, abstractmethod


"""Si vuole progettare un sistema in Python per la 
gestione delle prenotazioni aeree. Il sistema dovrà 
gestire diverse tipologie di voli, tra cui voli
commerciali e voli charter.
 
Classe astratta Volo:
Tale classe sarà utilizzata per
definire nel suo costruttore le funzionalità base 
di ogni tipo di volo, come il codice del volo
(stringa) e la capacità massima di posti 
disponibili sul volo (numero intero) che
sono attributi passati come argomenti in input. 
Inoltre, la classe deve avere un attributo chiamato 
prenotazioni, il quale non deve essere passato come argomento 
del costruttore; il costruttore, però, deve assegnare valore iniziale
pari a 0 a tale attributo.
 
Metodi:

    si definisca il metodo astratto prenota_posto().
    si definisca il metodo astratto posti_disponibili()."""


class AbcVolo(ABC):
    def __init__(self,codice_volo: int, max_posti:int) -> None:

        self.codice_volo = codice_volo
        self.max_posti = max_posti
        self.prenotazioni = 0


    @abstractmethod
    def prenota_posto(self):
        pass
    
    @abstractmethod
    def posti_disponibili(self):
        pass


class VoloCommerciale(AbcVolo):
    def __init__(self, codice_volo: int, max_posti: int) -> None:
        super().__init__(codice_volo, max_posti)

        self.posti_economica = max_posti * 0.7
        self.posti_business = max_posti * 0.2
        self.posti_prima = max_posti -(self.posti_economica + self.prenotazioni_business)
        self.prenotazioni_economica = 0
        self.prenotazioni_business = 0
        self.prenotazioni_prima = 0

    
    def prenota_posto(self, posti: int, classe_servizio):
            if posti :

             pass
    
    def posti_disponibili(self) -> dict:
        diz: dict = {}
        diz['posti disponibili'] = self.max_posti
        diz['post_econimica'] = self.posti_economica
        diz['posti_business'] = self.posti_business
        diz['posti_prima'] = self.posti_prima

        
    
     """"   che consente di prenotare un certo numero di posti
     sul volo in una determinata classe. Tale metodo, 
     prima di riservare un posto, deve controllare prima 
     che ci siano posti disponibili sull'intero volo, poi 
     se ci sono posti disponibili nella classe richiesta. 
      In caso affermativo, contare il numero dei posti prenotati
         in tale classe. Inoltre, nel caso in cui sia possibile 
        prenotare un posto, il metodo deve stampare a schermo un 
        messaggio che notifichi all'utente di aver riservato un 
        tot di posti per una determinata classe su un dato volo 
(specificando il codice del volo). In caso contrario, stampare a 
     schermo un messaggio che notifichi all'utente che non ci sono più
     posti disponibili nella classe scelta. Se sul volo non ci sono più posti
  disponibili, il metodo deve stampare a schermo un messaggio notificando
      all'utente che il volo è al completo. Inoltre, se la classe passata 
     come input del metodo non risulta essere una delle seguenti classi 
     ("economica", "business", "prima"), il metodo deve stamapre a schermo 
             un messaggio di errore, notificando all'utente che la classe richiesta 
         non è valida. Infine, il metodo deve aggiornare l'attributo prenotazioni 
    della classe estesa Volo, sommando il numero di prenotazioni
      ricevute per ogni classe di servizio, poi aggiornare gli attributi
        prenotazioni_economica, prenotazioni_business, prenotazioni_prima 
        con l'esatto numero delle prenotaioni ricevute per ogni 
        classe di servizio. Suggerimento: introdurre delle variabili 
        locali d'appoggio per gestire le prenotazioni per ogni classe di 
        servizio da azzerare all'inizio di ogni fase di prenotazione."""
        pass