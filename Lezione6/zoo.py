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

    def set_width (self, width) -> float:
        self.width = width    

    def get_width (self) -> float:
        return self.width    

    def set_height (self, height) -> float:
        self.height = height    

    def get_height (self) -> float:
        return self.height   

    def set_health (self, health) -> float:
        self.health = health

    def get_health (self) -> float:
        return self.health   
    
    def get_area_animal (self) -> float:
        return self.get_width() * self.get_height()

    def feed (self) -> float:
        self.set_health(self.get_health() / 100 * 101) 
        self.set_width(self.get_width() / 100 * 102)      
        self.set_height(self.get_height() / 100 * 102)   

    
    def __str__(self) -> str:
        return (f'{self.name.capitalize()} (species = {self.species}, age = {self.age} height = {self.height}'
                + f' width = {self.width} preferred habitat = {self.preferred_habitat} health ={self.health}'
                +f' area animale {self.animal_area}')   
       
class Fence:
    def __init__(self, area : float, temperature : float, habitat : str):

        self.area : float = area
        self.temperature : float = temperature
        self.habitat : str = habitat
        self.lista_animali_recinto: list= []
        
    def get_area_free (self):
        area_occupata = sum(animale.get_area_animal() for animale in self.lista_animali_recinto)
        return self.area - area_occupata
    
    def get_animal_names(self):
        return [animale.name for animale in self.lista_animali_recinto]

    def __str__(self) -> str:
        return f'area = {self.area} temperature = {self.temperature}, habitat = {self.habitat} lista animale recinto ={self.lista_animali_recinto}'

class ZooKeeper:

    def __init__(self, nome : str, cognome : str, id: float):
         
        self.nome : float = nome
        self.cognome : float = cognome
        self.id : str = id

    def add_animal(self, animal : Animal, fence: Fence) : 

        area_libera = fence.get_area_free()

        if animal.get_area_animal() <= area_libera and animal.preferred_habitat == fence.habitat:
            fence.lista_animali_recinto.append(animal)
            print(f"{animal.name} è stato aggiunto alla gabbia")

        elif animal.get_area_animal() > fence.area:
            print(f"{animal.name} l'animale è troppo grande per questa gabbia")

        elif animal.preferred_habitat != fence.habitat:
            print(f"{animal.name} l'habitat del animale non è adeguato a questa gabbia")
        

    def remove_animal(self, animal: Animal, fence : Fence):
          
          if animal in fence.lista_animali_recinto:
              fence.lista_animali_recinto.remove(animal)
              print(f"{animal.name} è stato rimosso dalla gabbia !")

          else:
              print("L'animale non è presente nel recinto.")

    def feed(self, animal: Animal): 
        animal.feed()

    def clean(fence: Fence) :
        for i in Fence:
        
            pass
     
    def __str__(self) -> str:
        return f'nome = {self.nome} cognome = {self.cognome}, id ={self.id}  '

# prove argomenti 
#animali
lupo = Animal("Lupo","lupus",7,30,20,"Foresta")
gatto_pallas = Animal("Gatto Pallas","Felide",4,15,10,"Steppa")
aquila = Animal("Aquila Reale","volatile",2,8,3,"Foresta")
cervo= Animal("cervo","cervide",4,30,11,"Foresta")
orso = Animal("orso","orside",4,300,3,"Foresta")
# fine animali

#fence
fence1 = Fence(300,25,"Steppa")
fence2 = Fence(1000,25,"Foresta")
# fine fence

#guardiani
franco = ZooKeeper("Franco","Minkia",333333)
# fine guardini 

print(f'{lupo}\n{gatto_pallas}\n{fence1}\n{franco}')
# prove argomenti fine 

# prove funzioni 

franco.add_animal(lupo, fence1)

print(fence1.get_animal_names())
print(fence1.get_area_free())

print(fence2.get_area_free())

franco.add_animal(lupo, fence2)

print(fence2.get_area_free())

franco.add_animal(aquila,fence2)

print(fence2.get_area_free())

franco.add_animal(orso,fence2)

print(fence2.get_animal_names())

franco.remove_animal(aquila,fence2)

print(fence2.get_animal_names())





