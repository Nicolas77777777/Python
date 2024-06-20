from persona import Persona

class Dottore(Persona):

    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float) -> bool:
        super().__init__(first_name, last_name)

        if isinstance(specialization,str):
            self.__specialization =  specialization
        else:
            self.__specialization = None
            print(f'La specializzazione inserita non è una stringa!')
            
        if isinstance(parcel,float):
            self.__parcel = parcel
        else: 
            self.__parcel = None
            print(f'La parcella inserita non è un float!')

        if isinstance(specialization, str) and (isinstance(parcel,float)):
            self.__parcel = parcel
            self.__specialization =  specialization

    def setSpecialization(self,specialization: str):
        if isinstance(specialization,str):
            self.__specialization = specialization
        else: 
            print(f'La specializzazione inserita non è una stringa!')
            
    def setParcel(self,parcel: float):
        if isinstance(parcel,float):
            self.__parcel = parcel
        else: 
            print(f'La parcella inserita non è un float!')

    def getSpecialization(self) -> str: 
       return self.__specialization
    
    def getParcel(self) -> float:
        return self.__parcel
    
    def isAValidDoctor(self) :
        if self.getAge() > 30:
            return f'Doctor {self.getName()} {self.getLastname()} is valid'
        else:
            return f'Doctor {self.getName()} {self.getLastname()} is not valid'

    def greet(self):
        print(f'Sono un Medico {self.__specialization}')


d1: Dottore = Dottore("Mario","Rossi","Ostretica",30.0)

d1.setAge(31)

print(d1.isAValidDoctor())