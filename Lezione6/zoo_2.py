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

    def getHheight (self) -> float:
        return self.height   

    def setHealth (self, health) -> float:
        self.health = health

    def getHealth (self) -> float:
        return self.health   


#####################

    def getArea (self) -> float:
        return self.getWidth() * self.getHheight()

    def feed (self) -> float:
        self.setHealth(self.getHealth() / 100 * 101)
        self.setWidth(self.getWidth() / 100 * 102)
        self.setHeight(self.getHheight() / 100 * 102)



class Fence:
    def __init__(self, area : float, temperature : float, habitat : str):

        self.area : float = area
        self.temperature : float = temperature
        self.habitat : str = habitat
        self.lista_animali_recinto: list= []

    def __str__(self) -> str:
        return f'area = {self.area} temperature = {self.temperature}, habitat = {self.habitat}'



class ZooKeeper:

    def __init__(self, nome : str, cognome : str, id: float):
         
        self.nome : float = nome
        self.cognome : float = cognome
        self.id : str = id
        self.area_recinto= None
        self.area_fence_animal_plus= 0
        self.area_fence_animal_minus= 0

    def add_animal(self, animal : Animal, fence: Fence) : 
        if animal.animal_area < fence.area and animal.preferred_habitat == fence.habitat:
            fence.lista_animali_recinto.append(animal.name)
            self.area_fence_animal_plus = animal.animal_area + fence.area
            print (f"{animal.name} è stato aggiunto alla gabbia")
        elif animal.animal_area > fence.area and animal.preferred_habitat == fence.habitat:
                 print (f"{animal.name} l'animale è troppo grande per questa gabbia")
        elif animal.animal_area < fence.area and animal.preferred_habitat != fence.habitat:
                  print(f"{animal.name} l'habitat del animale non è adeguato a questa gabbia")
        
    
    def remove_animal(self, animal: Animal, fence : Fence):
          if animal.name in fence.lista_animali_recinto:
              fence.lista_animali_recinto.remove(animal.name)
              self.area_fence_animal_minus= self.area_fence_animal_plus - animal.animal_area 
              print("L'animale è stato rimosso !")
          else:
              print("L'animale non è presente nel recinto.")

#    def feed (self, animal : Animal):
#            #if animal.animal_area < 
#                    animal.health += 1
#                    animal.height *= 1.02
#                    animal.width *= 1.02

    def clean(fence: Fence) :
        for i in Fence:
        
            pass
     
    def __str__(self) -> str:
        return f'nome = {self.nome} cognome = {self.cognome}, id ={self.id} '

    def feed(self, animal: Animal): 
        animal.feed()


cervo= Animal("cervo","cervide",4,30,11,"Foresta")
orso = Animal("orso","orside",4,300,3,"Foresta")
franco = ZooKeeper("Franco","Minkia",333333)

print(cervo)

franco.feed(cervo)


print(cervo)









