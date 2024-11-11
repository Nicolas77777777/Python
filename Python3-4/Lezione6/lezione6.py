# Exercise 1 
# definisco una classe con argomeneti \ Self è importante per atribuire argomenti alla classe

class Person:

    def __init__(self, name, age, height, weight):

        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.hobby: list[str]= []
    
# creo le persone con la funzione init
alice = Person("Alice W.", 45,187,60)
bob = Person("Bob M.", 36, 190, 120)

#stampo nome ed eta di bob 
print(bob.name, bob.age)

# stampo la persona piu giovane tra bob e Alice 
if alice.age > bob.age:
     print(alice.name,alice.age)
else:
    print(bob.name,bob.age) 


# creo una lista con l'utilizzo della classe 
persone = [alice,
            bob, 
            Person("davide",19,161,67), 
            Person("Flavio",29,160,49),
            Person("Simone",22,180,67)
            ]

# stampo la persona piu giovane nella lista con un ciclo 
min_age: int = float('inf') # numero infinito 
index_min_age: int = 0
# la funzione enumerate restituisce l'indice e l'oggetto 
for i, persona in enumerate(persone):
    if persona.age < min_age:
        min_age = persona.age
        index_min_age = i 

print(f'il nome della persona piu giovane è {persone[index_min_age].name}')

for i in range(len(persone)):
    if persone[i].age < min_age:
        min_age = persone[i].age
        index_min_age = i

print(f'il nome della persona piu giovane è {persone[index_min_age].name}'\
      + f' con eta {persone[index_min_age].age} altezza {persona.height} '\
        + f' peso {persona.weight}')


class Person2(Person):

    def __init__(self, name, age, height, weight):
        super().__init__(name, age, height, weight)


    def set_hobby(self, new_hobby: str):
        self.hobby.append(new_hobby)

    def __str__(self) -> str:
        return f'persona {self.name} {self.age} {self.height} {self.weight} {self.hobby}'
    

Eugenia= Person2('lorenzo',45,167,67)
Eugenia.set_hobby("pallacanestro")
Eugenia.set_hobby("karate")



print(Eugenia)



# 1:39

# ############################

# # Exercise 2 (Folder 9 ex_2.py)
# # 1. Write a class called Student with the attributes name (str) and
# # studyProgram (str)
# # 2. Create three instances. One for yourself, one for your left neighbour and one
# # for our right neighbour.
# # 3. Add a method printInfo that prints the name and studyProgram of a
# # Student. Test your method on the objects!
# # 4. Modify the code and add age and gender to the attributes. Modify your
# # printing methods respectively too.


# class Student:
#     def __init__(self, name: str, studyProgram :str, age: int, gender: str  ) -> None:
#         self.name = name
#         self.studyProgram = studyProgram
#         self.age = age
#         self.gender = gender
    
#     def printIn(self):
#         print(f" NOME:{self.name}: PROGRAMMA: {self.studyProgram} ETA: {self.age} GENERE: {self.gender}")

# me = Student("Nicola", "Cloud",20, "M")
# le = Student("Davide", "Cloud",34,"M")
# re = Student("Mauro", "Cloud",45,"F")


# me.printIn()
# le.printIn()
# re.printIn()


# # Exercise 3 (Folder 9 ex_3.py)
# # Given is the class Animal. For each task, test your changes!
# # 1. Create two realistic instances of Animals
# # 2. Print the name of each object
# # 3. Change the amount of legs of one object using the dot notation
# # 4. Add a method setLegs() to set the legs of an object and repeat task 3 but
# # this time using the method.
# # 5. Add a method getLegs() to return the amount of legs
# # 6. Add a method named printInfo that prints all attributes of the Animal


# # class Animal:
# #     def _init_ (self, name: str, legs:str):
# #         self.name = name
# #         self.legs =legs

# #     def get_legs (self):
# #         return self.legs
    
# #     def set_legs (self, x:int):
        

# #     # def __str__(self) -> str:
    
# #     #     pass


# # Exercise 4 (Folder 9 ex_4.py)
# # 1. Write a new class called Food, it should have name, price and
# # description as attributes.
# # 2. Instantiate at least three different foods you know and like.
# # 3. Create a new class called Menu, it should have a list (of Foods) as attribute.
# # __init__ should take a list of Foods as optional parameters (default=[])
# # 4. Create a addFood() and removeFood() for the Menu
# # 5. Create a few new Food instances. Add each to the Menu using the respective
# # Method.
# # 6. Add a method printPrices() that list all items on the Menu with their
# # prices.
# # 7. Add a Menu method getAveragePrice() that returns the average Food
# # price of the Men


# # class Food:

# #     def _init_  (self, name: str, price: int, descr:str ):
# #         self.name = name 
# #         self.price = price 
# #         self.descr = descr


# # pecorino = Food("Pecorino",3, "formaggio")
# # pizza = Food ("pizza",6, "farina e acqua")
# # Tonno = Food ("Tonno",14, "pesce")

# # class Menu:

# #     def _init_ (self,lista:list[Food]=[]):
# #         self.lista= lista

# #     def addFood(self, AddFood):
# #         AddFood
        
        

    
class Food:
    def __init__(self, name: str, price: float, description: str = None):
        self.name: str = name
        self.price: float = price
        self.description: str = description

    def __str__(self) -> str:
        return f'{self.name.capitalize()}(price={self.price}, descr={self.description})'

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