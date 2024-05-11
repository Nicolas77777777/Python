

# Creaiamo un sistema di gestione di uno zoo virtuale

# Sistema di gestione dello zoo virtuale

# Classi:

# 1. Zoo: questa classe rappresenta uno zoo. 
# Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.

# 2. Animal: questa classe rappresenta un animale nello zoo.
#   Ogni animale ha questi attributi: name, species, 
# age, height, width, preferred_habitat, health che è uguale a 100 * (1 / age).

# 3. Fence: questa classe rappresenta un recinto dello zoo in 
# cui sono tenuti gli animali. I recinti possono contenere uno o 
# più animali. I recinti possono hanno gli attributi area, temperature e habitat.

# 4. ZooKeeper: questa classe rappresenta un guardiano dello 
# zoo responsabile della gestione dello zoo. 
# I guardiani dello zoo hanno un nome, un cognome, e un id. 
# Essi possono nutrire gli animali, pulire i recinti e
# svolgere altri compiti nel nostro zoo virtuale.


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
        

    def __str__(self) -> str:
        return (f'{self.name.capitalize()} (species = {self.species}, age = {self.age} height = {self.height}'
                + f'width ={self.width} preferred habitat = {self.preferred_habitat} health ={self.health})')
    
   
       
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
        self.animali: list = [] 
    


    def add_animal(animal: Animal, fence: Fence):
        fence_list=[]

        pass


    def remove_animal(animal: Animal, fence: Fence):
        pass


    def feed (self, animal : Animal):

        self.animal_area : float = animal.height * animal.width

        return self.animal_area
    
    def __str__(self) -> str:
        return f'nome = {self.nome} cognome = {self.cognome}, id ={self.id} '
    
class Zoo:

    def __init__(self) -> None:
        pass

    def _str_():
        return
        pass
    

# prove argomenti
 
lupo = Animal("Lupo","lupus",7,30,20,"Foresta")
gatto_pallas = Animal("Gatto Pallas","Felide",4,15,10,"Steppa")
fence1 = Fence(100,25,"Steppa")
franco = ZooKeeper("Franco","Minkia",333333)


print(f'{lupo.__str__()}\n{gatto_pallas.__str__()}\n{fence1}\n{franco.__str__()}')

franco.feed(gatto_pallas)

print 


# prove argomenti fine 