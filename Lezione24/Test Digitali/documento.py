class Documento:
    def __init__(self,testo:str) -> None:
        self.testo= testo


    def setText(self,testo: str) -> None:
        self.testo = testo

    def getText (self) -> str:
        return self.testo
    

    def isInText(self, word:str) ->bool:
        if word.lower() in self.testo:
            print(True)
            return True

    def __str__(self) -> str:
        return f'nome {self.getText()}'

documento:Documento= Documento("porco il clero")
print(documento)

documento.isInText("porco")

