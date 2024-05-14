class Animal:
    def __init__(self, name : str, species : str,
                age : float, height : float,
                width : float, preferred_habitat: str,
                ):

        self.name: str = name
        self.species: str = species
        self.age: float = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat = preferred_habitat
        self.health= round( 100 * (1 / age),3)
        self.animal_area : float = height * width #area animale 
        
    def __str2__(self):
        print("NAME: "+str(self.name)+" AGE: "+str(self.age)+" WIDTH: "+str(self.width)+" HEIGHT: "+str(self.height)+" HEALTH: "+str(self.health))

    def __str__(self) -> str:
        return (f'{self.name.capitalize()} (species = {self.species}, age = {self.age} height = {self.height}'
                + f'width ={self.width} preferred habitat = {self.preferred_habitat} health ={self.health}'
                +f' area animale {self.animal_area}')   

    def setWidth (self, width) -> float:
        self.width = width    

    def getWidth (self) -> float:
        return self.width    

    def setHeight (self, height) -> float:
        self.height = height    

    def getHeight (self) -> float:
        return self.height   

    def setHealth (self, health) -> float:
        self.health = health

    def getHealth (self) -> float:
        return self.health   


#####################

    def getArea (self) -> float:
        return self.getWidth() * self.getHeight()

    def feed (self) -> float:
        self.setHealth(self.getHealth() / 100 * 101)
        self.setWidth(self.getWidth() / 100 * 102)
        self.setHeight(self.getHeight() / 100 * 102)


class Fence:
    def __init__(self, area : float, temperature : float, habitat : str):

        self.area : float = area
        self.temperature : float = temperature
        self.habitat : str = habitat
        self.animals: list= []

    def __str__(self) -> str:
        return f'area = {self.area} temperature = {self.temperature}, habitat = {self.habitat}'

    def __str2__(self) -> str:
        print("AREA: "+str(self.area)+" TEMPERATURA: "+str(self.temperature)+" HABITAT: "+self.habitat)
        for animal in self.animals:
            animal.__str2__()

    def getFreeArea(self) -> float:
        busy = 0
        for animal in self.animals:
            busy = busy + animal.getArea()
        return self.area - busy     
 
    def add_animal(self, animal: Animal):
        if self.getFreeArea() < animal.getArea():
            print('Impossibile aggiugere '+animal.name+' per area')  
        elif self.habitat != animal.preferred_habitat:
            print('Impossibile aggiugere '+animal.name+' per habitat')    
        else: 
            fence.animals.append(animal)

    def remove_animal(self, animal: Animal):
         for current_animal in self.animals:
            if current_animal.name == animal.name and current_animal.preferred_habitat == animal.preferred_habitat and current_animal.age == animal.age:
                self.animals.remove(current_animal)

class ZooKeeper:

    def __init__(self, nome : str, cognome : str, id: float):
         
        self.nome : float = nome
        self.cognome : float = cognome
        self.id : str = id
        self.area_recinto= None
        self.area_fence_animal_plus= 0
        self.area_fence_animal_minus= 0

    def add_animal(self, animal: Animal, fence: Fence):
        fence.add_animal(animal)        
    
#    def remove_animal(self, animal: Animal, fence : Fence):
#          if animal.name in fence.lista_animali_recinto:
#              fence.lista_animali_recinto.remove(animal.name)
#              self.area_fence_animal_minus= self.area_fence_animal_plus - animal.animal_area 
#              print("L'animale è stato rimosso !")
#          else:
#              print("L'animale non è presente nel recinto.")

    def remove_animal(self, animal: Animal, fence: Fence):
        fence.remove_animal(animal)


    def clean(fence: Fence) :
        for i in Fence:
        
            pass
     
    def __str__(self) -> str:
        return f'nome = {self.nome} cognome = {self.cognome}, id ={self.id} '

    def feed(self, animal: Animal): 
        animal.feed()



###
###
###
###


franco = ZooKeeper("Franco", "Minkia", 333)
orso = Animal("orso", "orside", 4, 30, 20, "Foresta")
castoro = Animal("castoro", "orside", 4, 10, 15, "Foresta")
lion = Animal("lion", "cat", 4, 10, 15, "Foresta")


#print(f'{orso.__str__()}')
franco.feed(orso)
#print(f'{orso.__str__()}')

fence = Fence(1000,25,"Foresta")
#print(f'{fence.__str__()}')
#fence.__str2__()
franco.add_animal(orso, fence)
fence.__str2__()
franco.add_animal(castoro, fence)
#franco.add_animal(castoro, fence)
fence.__str2__()
franco.add_animal(lion, fence)
fence.__str2__()
franco.remove_animal(orso, fence)
fence.__str2__()
franco.remove_animal(castoro, fence)
fence.__str2__()
franco.remove_animal(lion, fence)
fence.__str2__()
#print(f'{orso.__str__()}')
#print(fence.getFreeArea())

