from documento import Documento

""""Si definisca poi una classe Email che sia derivata da Documento
 e che includa le variabili per il mittente, il destinatario e il titolo del messaggio.
Si implementino i metodi get() e set() appropriati per tali variabili.
 Il corpo del messaggio dell’e-mail dovrebbe essere memorizzato nella
 variabile ereditata testo.
Si ridefinisca il metodo getText() per concatenare e ritornare tutti i
 campi di testo (mittente, destinatario, titolo del messaggio, e messaggio) come di seguito:
 
Da: alice@example.com, A: bob@example.com
Titolo: Incontro
Messaggio: Ciao Bob, possiamo incontrarci domani?
 
Inoltre, si implementi un metodo writeToFile() per scrivere il risultato del metodo getText() in un file
 di testo e in un percorso specificato."""

class Email(Documento):
    def __init__(self, testo: str,mittente: str, destinatario:str, titolo_messaggio: str ) -> None:
        super().__init__(testo)

        self.mittente = mittente
        self.destinatario= destinatario
        self.titolo_messaggio= titolo_messaggio

    # metodi set 

    def setMittente(self,mittente: str) -> None:
        self.mittente = mittente

    def setDestinatario(self,destinatario: str) -> None:
        self.destinatario = destinatario


    def setTitoloMessaggio(self,tit_mes: str) -> None:
        self.titolo_messaggio = tit_mes

    # metodi get
    
    def getMittente(self) -> str:
        return self.mittente

    def getDestinatario(self) -> str:
        return self.destinatario 


    def getTitoloMessaggio(self) -> str:
        return self.titolo_messaggio
    

    def __str__(self) -> str:
        return f'Mittente {self.mittente} destinatario{self.destinatario} Titolo messaggio {self.titolo_messaggio}'
    

    def getText(self):
        print ( f'Da {self.getMittente()} A{self.getDestinatario()}')



email:Email=Email("Ciao Bob, possiamo incontrarci domani?","alice@example.com","bob@example.com","Incontro",)

print 