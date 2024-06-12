
"""Vogliamo gestire un contatore che può essere incrementato,
 decrementato, resettato e visualizzato. La classe offre
un modo semplice per tenere traccia di un conteggio 
che non può diventare negativo.

Classe Contatore
Attributi:
- conteggio: un intero che conserva il valore del conteggio, inizializzato a 0.

Metodi:
- __init__(): Inizializza l'attributo conteggio a 0.
- setZero(): Imposta il conteggio a 0.
- add1(): Incrementa il conteggio di 1.
- sub1(): Decrementa il conteggio di 1, ma non permette che il conteggio diventi negativo.
 Se il conteggio è già 0, stampa un messaggio di errore.
- get(): Restituisce il valore corrente del conteggio.
- mostra(): Stampa a schermo il valore corrente del conteggio."""

class Contatore:
    def __init__(self):
        self.conteggio = 0
    
    def setZero(self):
        self.conteggio = 0
    
    def add1(self):
        self.conteggio += 1
    
    def sub1(self):
        if self.conteggio > 0:
            self.conteggio -= 1
        else:
            print("Non è possibile eseguire la sottrazione")
    
    def get(self):
        return self.conteggio
    
    def mostra(self):
        print(f"Conteggio attuale: {self.conteggio}")

# Esempio di utilizzo della classe
contatore = Contatore()
contatore.mostra()  # Output: Il valore corrente del conteggio è: 0
contatore.add1()
contatore.add1()

contatore.add1()

contatore.mostra()  # Output: Il valore corrente del conteggio è: 1
contatore.sub1()
contatore.mostra()  # Output: Il valore corrente del conteggio è: 0
contatore.sub1()    # Output: Errore: il conteggio è già 0 e non può essere decrementato.



"""" In questo esercizio, creeremo una gerarchia di classi per rappresentare
 diversi tipi di veicoli.
1. Classe Base: Veicolo
Crea una classe base chiamata Veicolo con i seguenti attributi e metodi:
 
Attributi:

    marca (stringa)
    modello (stringa)
    anno (intero)

Metodi:

    __init__(self, marca, modello, anno): metodo costruttore 
    che inizializza gli attributi marca, modello e anno.
    descrivi_veicolo(self): metodo che stampa una descrizione 
    del veicolo nel formato "Marca: [marca], Modello: [modello], Anno: [anno]"."""

class Veicolo:
    def __init__(self, marca: str, modello: str, anno: int ) :
        self.marca = marca
        self.modello= modello 
        self.anno = anno

    def descrivi_veicolo(self):
        descrivi = f'Marca: {self.marca}, Modello:{self.modello}, Anno: {self.anno}'
        return descrivi 
      


veicolo = Veicolo("Generic", "Model", 2020)
print(veicolo.descrivi_veicolo())
"""auto = Auto("Toyota", "Corolla", 2021, 4)
moto = Moto("Yamaha", "R1", 2022, "sportiva")

 
auto.descrivi_veicolo()
moto.descrivi_veicolo()"""

"""2. Classe Derivata: Auto
Crea una classe derivata chiamata Auto che eredita dalla
 classe Veicolo e aggiunge i seguenti attributi e metodi:
 
Attributi:

    numero_porte (intero)

Metodi:

    __init__(self, marca, modello, anno, numero_porte): 
    metodo costruttore che inizializza gli attributi della 
    classe base e numero_porte.
    descrivi_veicolo(self): metodo che sovrascrive
    quello della classe base per includere anche il numero di porte nella descrizione,
    nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Numero di porte: [numero_porte]"."""
class Auto(Veicolo):

    def __init__(self, marca: str, modello: str, anno: int, numero_porte: int):
        super().__init__(marca, modello, anno)

        self.numero_porte = numero_porte


    def descrivi_veicolo(self):
        descrivi = f'Marca: {self.marca}, Modello:{self.modello}, Anno: {self.anno} Numero di porte: '
        return descrivi 






"""3. Classe Derivata: Moto
Crea una classe derivata chiamata Moto che eredita dalla 
classe Veicolo e aggiunge i seguenti attributi e metodi:
 
Attributi:

    tipo (stringa, ad esempio "sportiva", "cruiser", ecc.)

Metodi:

    __init__(self, marca, modello, anno, tipo): metodo costruttore che inizializza gli attributi della classe base e tipo.
    descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il tipo di moto nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Tipo: [tipo]"."""

