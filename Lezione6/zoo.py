class Animal:

    total_animal=0
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
        self.animal_area : float = height * width
        self.fence: Fence= None
        Animal.total_animal += 1

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
    

    def get_total(cls):
        print (f'{cls.total_animal}')
    
    
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
        print ("l'area nel recinto rimannete è " )
        return self.area - area_occupata
    
    def get_area_busy (self):
        area_occupata = sum(animale.get_area_animal() for animale in self.lista_animali_recinto)
        return  area_occupata
    
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
            animal.fence = fence
            print(f"{animal.name} è stato aggiunto alla gabbia")

        elif animal.get_area_animal() > fence.area:
            print(f"{animal.name} l'animale è troppo grande per questa gabbia")

        elif animal.preferred_habitat != fence.habitat:
            print(f"{animal.name} l'habitat del animale non è adeguato a questa gabbia")
        
        elif animal.get_area_animal() < fence.area and animal.get_area_animal() > area_libera:
            print(f"ci sono troppi animale per questa gabbia {animal.name}")
        

    def remove_animal(self, animal: Animal, fence : Fence):
          if animal in fence.lista_animali_recinto:
              fence.lista_animali_recinto.remove(animal)
              print(f"{animal.name} è stato rimosso dalla gabbia !")

          else:
              print("L'animale non è presente nel recinto.")

    def feed(self, animal: Animal):

        area_occupata_da_animali: float = 0.0
        for a in animal.fence.lista_animali_recinto:
        
              if animal.get_area_animal() < animal.get_area_animal():
                new_health = round(animal.get_health() / 100 * 101, 2)
                new_width = round(animal.get_width() / 100 * 102, 2)
                new_height = round(animal.get_height() / 100 * 102, 2) 
        
    
    def clean(fence: Fence) :
        area_residua = fence.get_area_free()
        area_occupata = fence.get_area_busy()
        if area_residua == 0:
            return area_occupata
        else:
            return area_occupata / area_residua
     
    def __str__(self) -> str:
        return f'nome = {self.nome} cognome = {self.cognome}, id ={self.id} '
        
    

class Zoo:
    def __init__(self):
        self.fences = []  
        self.zoo_keepers = []  


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

#print(f'{lupo}\n{gatto_pallas}\n{fence1}\n{franco}')
# prove argomenti fine 

# prove funzioni 

franco.add_animal(lupo, fence1)

print(fence1.get_animal_names())
# print(fence1.get_area_free())

# print(fence2.get_area_free())

franco.add_animal(lupo, fence2)

print(fence2.get_area_free())

franco.add_animal(aquila,fence2)

print(fence2.get_area_free())

franco.add_animal(orso,fence2)

print(fence2.get_animal_names())

franco.remove_animal(aquila,fence2)

print(fence2.get_animal_names())

franco.feed(lupo)

# print(lupo )

# franco.feed(lupo)
# print(lupo)

# Animal.get_total(Animal)

#franco.feed(lupo)
