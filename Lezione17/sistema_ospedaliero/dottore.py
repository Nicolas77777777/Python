from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float) -> bool:
        super().__init__(first_name, last_name)

        if isinstance(specialization,str):
            self.__specialization =  specialization
        else:
            self.__specialization = None
            print(f'Il nome inserito non è una stringa!')
            
        if isinstance(parcel,float):
            self.__last_name = last_name
        else: 
            self.__first_name = None
            self.__eta = None
            print(f'Il nome inserito non è una stringa!')

        if isinstance(first_name, str) and (isinstance(last_name, str)):
            self.__eta = 0

    def setName(self, first_name:str):
        if isinstance(first_name,str):
            self.__first_name = first_name
        else: 
            print(f'Il nome inserito non è una stringa!')
            
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