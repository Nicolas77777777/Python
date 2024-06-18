from persona import Persona

class Dottore(Persona):
    def __init__(self, specialization: str, last_name: str, specialization: str, parcel: float) -> bool:
        super().__init__(specialization, last_name)

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

    def setSpecialization(self, specialization:str):
        if isinstance(specialization,str):
            self.__specialization = specialization
        else: 
            print(f'La specializzazione inserita non è una stringa!')
            
    def setLastName(self, last_name: str ) -> str:
        if isinstance(last_name,str):
            self.__last_name = last_name
        else: 
            print(f'Il nome inserito non è una stringa!')

    def setAge(self, age: int) -> int:
        if isinstance(age,int):
            self.__eta = age
        else: 
            print(f'Il nome inserito non è una stringa!')

    def getName(self) -> str: 
       return self.setName()
    
    def getLastname(self) -> str:
        return self.setLastName()
      
    def getAge(self) -> int:
        return self.setAge()
    
    def greet(self):
        print(f'Ciao sono {self.__first_name} {self.__last_name}! Ho {self.__eta}')