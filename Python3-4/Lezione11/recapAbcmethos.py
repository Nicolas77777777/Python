from abc import ABC, abstractmethod


class AbcAnimal(ABC):

    @abstractmethod
    def verso(self):

        pass

class Cane(AbcAnimal):

    def __init__(self, nome: str) -> None:
        self.name: str = nome

    def verso(self):
        print(f"Bau")



class Gatto(AbcAnimal):

    def __init__(self, nome: str) -> None:
        self.name: str = nome

    def verso(self):
        print(f"MIao")


class Coccodrillo(AbcAnimal):

    def __init__(self, nome: str) -> None:
        self.name: str = nome

    def verso(self):
        print(f"brrr")

from typing import Any # quando si imposta su typeCheck è utile impostare questa libreria 
from typing import TypeAlias # rinomina 

tipocomposto : TypeAlias = dict[int, Any]

a: dict[str, Any] = {

    "key_1" : "val_1",
    "key_2" : "val_2",
    "key_3" : 3,
    "key_4" : [1,2]

}

cane_1: Cane = Cane(nome="pluto")

cane_1.verso()

gatto_1: Gatto = Gatto(nome="Silvestro")

gatto_1.verso()

coccodrillo_1: Coccodrillo = Coccodrillo(nome="GIOVANNI")

coccodrillo_1.verso()



lista_animali: list[AbcAnimal]= [cane_1, gatto_1, coccodrillo_1]

for animale in lista_animali:
    
    animale.verso()

