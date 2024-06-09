""" Implementare una classe Media che rappresenti un media generico 
(ad esempio, un film o un libro) e una classe derivata Film che 
rappresenti specificamente un film. Gli studenti dovranno anche 
creare oggetti di queste classi, aggiungere valutazioni e visualizzare 
le recensioni.

Specifiche della Classe Media:
 
Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media,
 con voti compresi tra 1 e 5, dove 1=Terribile, 2=Brutto, 3=Normale, 4=Bello, 5=Grandioso.

Metodi:
- set_title(self, title): Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione 
  alla lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio
   medio basato sulla media delle valutazioni, ovvero mostra "Terribile" 
   se il voto medio si avvicina a 1, "Brutto" se il voto medio si avvicina a 2,
  "Normale" se il voto medio si avvicina a 3, "Bello" se il voto medio si avvicina a 4,
 "Grandioso" se il voto medio si avvicina a 5.
- ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto 
  specifico nelle recensioni.
- recensione(self): Mostra un riassunto delle recensioni e delle valutazioni 
 del media, stampando il titolo, il voto medio, il giudizio e le percentuali
 di ciascun voto. Esempio di riassunto:
 
Titolo del Film: The Shawshank Redemption
Voto Medio: 3.80
Giudizio: Bello
Terribile: 10.00%
Brutto: 10.00%
Normale: 10.00%
Bello: 30.00%
Grandioso: 40.00%

Si verifichi il funzionamento scrivendo un codice che crei 
almeno due oggetti di tipo Film, aggiunga a ognuno dei due almeno 
dieci valutazioni e richiami il metodo recensione().
"""


class Media:
    def __init__(self) :
        self.title = ""
        self.reviews = []


    def set_title(self, title: str) -> str: 
        self.title = title


    def get_title(self) -> str: 
        return  self.title
    

    def  aggiungiValutazione(self, voto: int) -> list:
        if voto != 0 and voto <= 5 :
            self.reviews.append(voto)
            return self.reviews
        else:
            print (f'aggiungi un valore compreso tra 1 e 5 ')


    def getMedia(self) -> float : 
        return sum(self.reviews) / len(self.reviews)
    

    def getRate(self) -> str:
        media = self.getMedia()
        if media <= 1.5:
            return "Terribile"
        elif media < 2.5 :
            return " Brutto"
        elif media < 3.5:
            return "Normale"
        elif media < 4.5:
            return  "Bello"
        elif media  <= 5:
            return " Grandioso"

    def ratePercentage(self, voto : int)  -> float:
        media = 0 
        for n in self.reviews:
            if n == voto:
                media = (self.reviews.count(n) / len(self.reviews))*100
        return f'{media}%' 
    
          
    def recensione(self) -> str :
       print(f'Titolo Film: {self.get_title()}\n Voto Medio: {self.getMedia()}\n Giudizio: {self.getRate}')
        


    def __str__(self) -> str:
        return f' Titolo Film {self.get_title()} Voto Medio {self.getMedia()} Giudizio: {self.getRate})'


class Film(Media):

    def __init__(self) -> None:
        super().__init__()



film1: Film = Film()
Film.set_title(film1,"Balla coi Lupi")
Film.get_title(film1)

film1.aggiungiValutazione(5)
print(film1.reviews)
film1.aggiungiValutazione(4)
print(film1.reviews)
film1.aggiungiValutazione(2)
print(film1.reviews)
film1.aggiungiValutazione(1)
print(film1.reviews)
film1.aggiungiValutazione(3)
print(film1.reviews)


film1.getRate()
print(film1)
print(film1.getRate())


film1.ratePercentage(5)

print(film1.recensione())







    


    

    


