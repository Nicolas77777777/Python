from persona import Persona

class Paziente(Persona):
    def __init__(self, first_name: str, last_name: str, idCode: str) -> bool:
        super().__init__(first_name, last_name)

        self.__idCode = idCode

    def setIdCode(self,idCode) -> None:
        self.__idCode = idCode

    def getidCode(self) -> str:
        return self.__idCode
    
    def patientInfo(self):
        print(f'Paziente {self.getName()} {self.getLastname()}')
        print(f'ID: {self.__idCode}')

s:Paziente = Paziente("Franco","Minkia","11233")

s.patientInfo()





