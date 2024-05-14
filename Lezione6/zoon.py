class Animal:
    def __init__(self, name: str, species: str, age: float, height: float, width: float, preferred_habitat: str):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)
        self.animal_area = height * width

    def set_width(self, width) -> float:
        self.width = width    

    def get_width(self) -> float:
        return self.width    

    def set_height(self, height) -> float:
        self.height = height    

    def get_height(self) -> float:
        return self.height   

    def set_health(self, health) -> float:
        self.health = health

    def get_health(self) -> float:
        return self.health   
    
    def get_area_animal(self) -> float:
        return self.get_width() * self.get_height()

    def __str__(self) -> str:
        return (f'{self.name.capitalize()} (species = {self.species}, age = {self.age} height = {self.height}'
                + f' width = {self.width} preferred habitat = {self.preferred_habitat} health ={self.health}'
                + f' area animale {self.animal_area}')


class Fence:
    def __init__(self, area: float, temperature: float, habitat: str):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.lista_animali_recinto = []

    def get_area_free(self):
        area_occupata = sum(animale.get_area_animal() for animale in self.lista_animali_recinto)
        return self.area - area_occupata
    
    def get_area_busy(self):
        area_occupata = sum(animale.get_area_animal() for animale in self.lista_animali_recinto)
        return area_occupata
    
    def get_animal_names(self):
        return [animale.name for animale in self.lista_animali_recinto]

    def __str__(self) -> str:
        return f'area = {self.area} temperature = {self.temperature}, habitat = {self.habitat} lista animale recinto ={self.lista_animali_recinto}'


class ZooKeeper:
    def __init__(self, name: str, surname: str, id: float):
        self.name = name
        self.surname = surname
        self.id = id

    def add_animal(self, animal: Animal, fence: Fence):
        area_libera = fence.get_area_free()
        if animal.get_area_animal() <= area_libera and animal.preferred_habitat == fence.habitat:
            fence.lista_animali_recinto.append(animal)
            print(f"{animal.name} è stato aggiunto alla gabbia")
        elif animal.get_area_animal() > fence.area:
            print(f"{animal.name} l'animale è troppo grande per questa gabbia")
        elif animal.preferred_habitat != fence.habitat:
            print(f"{animal.name} l'habitat del animale non è adeguato a questa gabbia")
        
    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.lista_animali_recinto:
            fence.lista_animali_recinto.remove(animal)
            print(f"{animal.name} è stato rimosso dalla gabbia !")
        else:
            print("L'animale non è presente nel recinto.")

    def feed(self, animal: Animal):
       
        for fence in animal.fences:
            if animal in fence.lista_animali_recinto:
             if animal.name in Fence.lista_animali_recinto:
                if animal.get_area_animal() < animal.get_area_animal():
                    new_health = round(animal.get_health() / 100 * 101, 2)
                    new_width = round(animal.get_width() / 100 * 102, 2)
                    new_height = round(animal.get_height() / 100 * 102, 2) 

    def clean(self, fence: Fence):
        area_residua = fence.get_area_free()
        area_occupata = fence.get_area_busy()
        if area_residua == 0:
            return area_occupata
        else:
            return area_occupata / area_residua

    def __str__(self) -> str:
        return f'name = {self.name} surname = {self.surname}, id ={self.id}'

class Zoo:
    def __init__(self):
        self.fences = []  # Lista dei recinti dello zoo
        self.zoo_keepers = []  # Lista dei guardiani dello zoo

    def add_fence(self, fence):
        """Aggiunge un recinto allo zoo."""
        self.fences.append(fence)

    def add_zoo_keeper(self, zoo_keeper):
        """Aggiunge un guardiano allo zoo."""
        self.zoo_keepers.append(zoo_keeper)

    def describe_zoo(self):
        """Visualizza informazioni su tutto lo zoo."""
        print("Guardians:")
        for zoo_keeper in self.zoo_keepers:
            print(zoo_keeper)
        print("#" * 30)
        print("Fences:")
        for fence in self.fences:
            print(fence)
            if fence.lista_animali_recinto:
                print("with animals:")
                for animal in fence.lista_animali_recinto:
                    print(animal)
            print("#" * 30)


# Esempio di utilizzo:
zoo = Zoo()

# Aggiungi un recinto
fence1 = Fence(100, 25, "Continentale")
zoo.add_fence(fence1)

# Aggiungi un guardiano
keeper1 = ZooKeeper("Lorenzo", "Maggi", 1234)
zoo.add_zoo_keeper(keeper1)

# Aggiungi animali al recinto
scoiattolo = Animal("Scoiattolo", "Blabla", 25, 10, 5, "Alberi")
lupo = Animal("Lupo", "Lupus", 14, 20, 10, "Foresta")
keeper1.add_animal(scoiattolo, fence1)
keeper1.add_animal(lupo, fence1)

# Visualizza informazioni sullo zoo
zoo.describe_zoo()

keeper1.feed(lupo)
