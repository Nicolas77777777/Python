class Persona:

    def __init__(self, first_name: str,last_name: str) -> bool :
        

        if isinstance(first_name,str):
            self.__first_name = first_name
        else:
            self.__first_name = None
            print(f'Il nome inserito non è una stringa!')
            
        if isinstance(last_name,str):
            self.__last_name = last_name
        else: 
            self.__last_name = None
            print(f'Il cognome inserito non è una stringa!')

        self.__eta = None
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
            print(f' L età deve essere un numero intero!')

    def getName(self) -> str: 
       return self.__first_name
    
    def getLastname(self) -> str:
        return self.__last_name
      
    def getAge(self) -> int:
        return self.__eta
    
    def greet(self):
        print(f'Ciao sono {self.__first_name} {self.__last_name}! Ho {self.__eta}')
    
x:Persona = Persona("Franco","Rossi")

y:Persona = Persona(8,"Rossi")

x.setAge(20)

x.getName()


x.greet()

        
        




            


        




        
       
        
            
