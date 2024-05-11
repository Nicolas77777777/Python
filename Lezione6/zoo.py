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
       
class Fence:
    def __init__(self, area : float, temperature : float, habitat : str):

        self.area : float = area
        self.temperature : float = temperature
        self.habitat : str = habitat

    def __str__(self) -> str:
        return f'area = {self.area} temperature = {self.temperature}, habitat = {self.habitat}'

class ZooKeeper:

    def __init__(self, nome : str, cognome : str, id: float):
         
        self.nome : float = nome
        self.cognome : float = cognome
        self.id : str = id
        self.lista_recinto: list= []
        self.area_recinto= None
        self.area_fence_animal_plus= 0
        self.area_fence_animal_minus= 0
    
    def feed (self, animal : Animal):
       # self.animal_area : float = animal.height * animal.width
        return None

    def add_animal(self, animal : Animal, fence: Fence) : 
        if animal.animal_area < fence.area:
            if animal.preferred_habitat == fence.habitat:
                self.lista_recinto.append(animal.name)
                self.area_fence_animal_plus = animal.animal_area + fence.area
        else:
            print("non è possibile aggiungere l'animale poiche l'animale è troppo grande")
        
    
    def remove_animal(self, animal: Animal, fence : Fence):
          if animal.name in self.lista_recinto:
              self.lista_recinto.remove(animal.name)
              self.area_fence_animal_minus= self.area_fence_animal_plus - animal.animal_area 
              print("L'animale è stato rimosso !")
          else:
              print("L'animale non è presente nel recinto.")
             

    def __str__(self) -> str:
        return f'nome = {self.nome} cognome = {self.cognome}, id ={self.id} '

# prove argomenti 
lupo = Animal("Lupo","lupus",7,30,20,"Foresta")
gatto_pallas = Animal("Gatto Pallas","Felide",4,15,10,"Steppa")
fence1 = Fence(300,25,"Steppa")
# fence2 = Fence(1000,25,"Foresta")
franco = ZooKeeper("Franco","Minkia",333333)
print(f'{lupo.__str__()}\n{gatto_pallas.__str__()}\n{fence1}\n{franco.__str__()}')
# prove argomenti fine 

# prove funzioni 

franco.add_animal(lupo, fence1)
# franco.add_animal(lupo,fence2)

franco.add_animal(gatto_pallas, fence1)

print(franco.lista_recinto, franco.area_fence_animal_plus, " aggiungo animale")

franco.remove_animal(gatto_pallas, fence1)

r = franco.lista_recinto

print(franco.lista_recinto, franco.area_fence_animal_minus, "rimuovo animale")
print(r)









