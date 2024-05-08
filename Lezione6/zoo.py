

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

class Zoo:
    def __init__(self) -> None:
        pass


class Animals:
    def __init__(self, name : str, species : str, age : float, height : float, width : float):

        self.name: str = name
        self.species: str = species
        self.age: float = age
        self.height: float = height
        self.width: float = width

    def __str__(self) -> str:
        return f'{self.name.capitalize()}(species ={self.species}, age ={self.age} height = {self.height}\
           width ={self.width} )'
    

class Recinto :
    def __init__(self, dimension, temperature: float, habitat: str):
        self.dimension = dimension
        self.temperature: float = temperature
        self.habitat: str = habitat

    def __str__(self) -> str:
        return f'{self.dimension()}(temperature={self.temperature}, habitat ={self.habitat})'


class ZooKeeper :
class Menu:
    def __init__(self, foods: list[Food] = []):
        self.foods:list[Food] = foods
    
    def addFood(self, food: Food):
        # food_name in self.foods
        count: int = 0
        for food_menu in self.foods:
            if food.name == food_menu.name:
                count += 1
                food_menu.price = food.price
        if count == 0:
            self.foods.append(food)

    def removeFood(self, food: Food):
        if food in self.foods:
            self.foods.remove(food)
    
    def getAvgPrice(self) -> float:
        total_sum: float = 0
        for food in self.foods:
            total_sum += food.price
        # divido per la lunghezza della lista foods
        avg_price: float = total_sum/ len(self.foods)
        return avg_price

    def __str__(self) -> str:
        repr: str = ""
        for food in self.foods:
            repr += food.__str__() + "\n"
        avg_price: float = self.getAvgPrice()
        repr += "_" * 30 + "\n"
        repr += f'Prezzo medio = {avg_price}'
        return repr
    

carbonara = Food(name="Carbonara", price=10.5, description="La carbonara è buona")
cacio_e_pepe = Food(name="cacio_e_pepe", price=15.48)
un_altra_carbonara = Food(name="Carbonara", price=10.5, description="La carbonara è buona")

menu = Menu()
menu.addFood(carbonara)
menu.addFood(cacio_e_pepe)
menu.addFood(un_altra_carbonara)
print(menu.__str__())