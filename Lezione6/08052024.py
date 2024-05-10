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

from typing import Any


class Zoo:
    def __init__(self) -> None:
        pass


class Animals:
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
        self.health=  100 * (1 / age)


    def __str__(self) -> str:
        return f'{self.name.capitalize()}(species ={self.species}, age ={self.age} height = {self.height}\
           width ={self.width} preferred habitat = {self.preferred_habitat} health ={self.health})'
        

class Animals2(Animals):

    def __init__(self, name: str, species: str, age: float, height: float, width: float, preferred_habitat: str):
        super().__init__(name, species, age, height, width, preferred_habitat)

class Recinto :
    def __init__(self, dimension, temperature: float, habitat: str):
        self.dimension = dimension
        self.temperature: float = temperature
        self.habitat: str = habitat

    def __str__(self) -> str:
        return f'{self.dimension()}(temperature={self.temperature}, habitat ={self.habitat})'


class ZooKeeper :

    def __init__(self) -> None:
        pass



lupo= Animals("Fenfir","lupus",7,30,20,"Foresta")

print(lupo.__str__())


