"""" . GESTIONALE PAGAMENTO
Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo float 
che memorizza l'importo del pagamento e si definiscano appropriati metodi get() e set(). 
L'importo non è un parametro da passare in input alla classe Pagamento ma deve 
essere inizializzato utilizzando il metodo set() dove opportuno. 
Si crei inoltre un metodo dettagliPagamento() che visualizza una 
frase che descrive l'importo del pagamento, ad esempio: "Importo del pagamento: €20.00".
 Quando viene stampato, l'importo è sempre con 2 cifre decimali.

Successivamente, si definisca una classe PagamentoContanti che 
sia derivata da Pagamento e definisca l'importo. 
Questa classe dovrebbe ridefinire il metodo dettagliPagamento()
 per indicare che il pagamento è in contanti. 
 Si definisca inoltre il metodo inPezziDa() che stampa a schermo
quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro,
10 euro, 5 euro e/o in quante monete da 2 euro, 1 euro, 0,50 euro,
0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie
per pagare l'importo in contanti.

Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da
 Pagamento e che definisce l'importo. Questa classe deve contenere
gli attributi per il nome del titolare della carta, la data di scadenza,
e il numero della carta di credito. Infine, si ridefinisca il metodo
 dettagliPagamento() per includere tutte le informazioni della carta di 
 credito oltre all'importo del pagamento.

Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo 
PagamentoCartaDiCredito con valori differenti e si invochi dettagliPagamento() per ognuno di essi.

Esempio di output:
Pagamento in contanti di: €150.00
150.00 euro da pagare in contanti con:
1 banconota da 100 euro
1 banconota da 50 euro

Pagamento in contanti di: €95.25
95.25 euro da pagare in contanti con:
1 banconota da 50 euro
2 banconote da 20 euro
1 banconota da 5 euro
1 moneta da 0.2 euro
1 moneta da 0.05 euro

Pagamento di: €200.00 effettuato con la carta di credito
Nome sulla carta: Mario Rossi
Data di scadenza: 12/24
Numero della carta: 1234567890123456

Pagamento di: €500.00 effettuato con la carta di credito
Nome sulla carta: Luigi Bianchi
Data di scadenza: 01/25
Numero della carta: 6543210987654321"""

import math

class Pagamento:
    def __init__(self) :

        self.__importo:float= 0.0
    
    def setPagamento(self,importo):
        self.__importo = importo

    def getPagamento(self) -> float:
        return self.__importo


    def dettagliPagamento(self)-> str:
        print(f'Importo del pagamento è {self.getPagamento():.2f} ')
 

class PagamentoContanti(Pagamento):
    def __init__(self):
        super().__init__()

    def dettagliPagamento (self):
        print(f'Pagamento in contanti di {self.getPagamento():.2f} ')

    def inPezzida(self,importo):
        banconote:list =[500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01] # creo lista 
        how_many_banconote: dict = {} # creo dizionario vuoto per inseire chiave banconote e valore la quantita utilizzata
        resti = {} # dizionario vuoto per il resto della divisione 
        
        for banconota in banconote: # ciclo sulla lista banconote 
            
            how_many_banconote[banconota]=int(importo/banconota)
            resti[banconota] = math.fmod(importo,banconota)
            resto= math.fmod(importo,banconota)
            importo = resto
            print("quante banconote",how_many_banconote)

        for banconota, quantita in how_many_banconote.items():
            
            type : str = "banconota"
            types : str = "banconote"

            if banconota < 5:
                type : str = "moneta"
                types : str = "monete"
 
            if quantita  == 1 :
                print (f'{quantita} {type} da {banconota} euro') 
            elif quantita > 1:
                print (f'{quantita} {types} da {banconota} euro') 

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self):
        super().__init__()




pagamento:Pagamento= Pagamento()

pagamento.setPagamento(30)

print(pagamento.getPagamento())

pagamento.dettagliPagamento()


paga_contanti: PagamentoContanti= PagamentoContanti()

paga_contanti.inPezzida(1024)
paga_contanti.inPezzida(1025.25)
paga_contanti.inPezzida(95.25)

#paga_contanti.inPezzida(500)


#paga_contanti.inPezzida(234)



# def resto_divisione(x: float, y:float ):
#     resto= x % y
#     print(resto)
#     return resto

# resto_divisione(500,230)


    