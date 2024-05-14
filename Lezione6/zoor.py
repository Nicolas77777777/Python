class Animal:
    def __init__(self, name: str, species: str,
                 age: float, height: float,
                 width: float, preferred_habitat: str,
                 ):

        self.name: str = name
        self.species: str = species
        self.age: float = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat = preferred_habitat
        self.health: float = round(100 * (1 / age), 3)
        self.animal_area: float = height * width
        self.fence = None

    def __str2__(self):
        print("NAME: " + str(self.name) + " AGE: " + str(self.age) + " WIDTH: " + str(self.width) + " HEIGHT: " + str(
            self.height) + " HEALTH: " + str(self.health))

    def __str__(self) -> str:
        return (f'{self.name.capitalize()} (species = {self.species}, age = {self.age} height = {self.height}'
                + f'width ={self.width} preferred habitat = {self.preferred_habitat} health ={self.health}'
                + f' area animale {self.get_area()}')

    def set_width(self, width):
        self.width = width

    def get_width(self) -> float:
        return self.width

    def set_height(self, height):
        self.height = height

    def get_height(self) -> float:
        return self.height

    def set_health(self, health):
        self.health = health

    def get_health(self) -> float:
        return self.health

    #####################

    def get_area(self) -> float:
        return self.get_width() * self.get_height()

    def feed(self):
        newHealth = round(self.get_health() / 100 * 101, 2)
        newWidth = round(self.get_width() / 100 * 102, 2)
        newHeight = round(self.get_height() / 100 * 102, 2)

        if self.fence is None:
            self.set_health(newHealth)
            self.set_width(newWidth)
            self.set_height(newHeight)
            return

        areaDelta = (newWidth * newHeight) - self.get_area()

        if areaDelta <= self.fence.get_free_area():
            self.set_health(newHealth)
            self.set_width(newWidth)
            self.set_height(newHeight)
        else:
            print("Impossible to feed " + self.name + ". Not enough free area in " + str(self.fence.__str__()))


class Fence:
    def __init__(self, area: float, temperature: float, habitat: str):

        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.animals: list = []

    def __str__(self) -> str:
        return f'area = {self.area} temperature = {self.temperature}, habitat = {self.habitat}'

    def __str2__(self) -> str:
        print("AREA: " + str(self.area) + " TEMPERATURA: " + str(self.temperature) + " HABITAT: " + self.habitat + " FREE AREA: " + str(self.get_free_area()))
        if len(self.animals):
            print("With Animals")
        for animal in self.animals:
            print(f'{animal.__str__()}')
        print('##############################')

    def get_free_area(self) -> float:
        busy = 0
        for animal in self.animals:
            busy = busy + animal.get_area()
        return self.area - busy

    def add_animal(self, animal: Animal):
        if self.get_free_area() < animal.get_area():
            print('Impossible to add ' + animal.name + '. Not enough area available')
        elif self.habitat != animal.preferred_habitat:
            print('Impossible to add ' + animal.name + '. Habitat is not compatible')
        else:
            animal.fence = self
            self.animals.append(animal)

    def remove_animal(self, animal: Animal):
        for current_animal in self.animals:
            if current_animal.name == animal.name and current_animal.preferred_habitat == animal.preferred_habitat and current_animal.age == animal.age:
                self.animals.remove(current_animal)
                current_animal.fence = None
class ZooKeeper:

    def __init__(self, nome: str, cognome: str, id: float):
        self.nome: float = nome
        self.cognome: float = cognome
        self.id: str = id
        self.area_recinto = None
        self.area_fence_animal_plus = 0
        self.area_fence_animal_minus = 0

    def add_animal(self, animal: Animal, fence: Fence):
        fence.add_animal(animal)

    def remove_animal(self, animal: Animal, fence: Fence):
        fence.remove_animal(animal)

    def clean(fence: Fence):
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

fence = Fence(1000, 25, "Foresta")
orso = Animal("orso", "orside", 4, 30, 20, "Foresta")

franco.add_animal(orso, fence)

fence_savana = Fence(1000, 25, "SAVANA")
lion = Animal("Lambert", "Lion", 3, 20, 30, "SAVANA" )

franco.add_animal(lion, fence_savana)

fence.__str2__()
fence_savana.__str2__()

franco.remove_animal(lion, fence_savana)
fence_savana.__str2__()
