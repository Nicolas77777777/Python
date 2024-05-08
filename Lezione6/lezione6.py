#  using unit

class Mahābhārata:
    def __init__(self,name: str, family: str,) -> None:
        self.name = name
        self.family = family


Pandu = Mahābhārata("Pāṇḍu","Pāṇḍava")
Dhṛtarāṣṭra = Mahābhārata("Dhṛtarāṣṭra","Karuwa")


# alice = Person("Alice W.", 45)
# bob = Person("Bob M.", 36)

# print(bob.name, bob.age)

# if alice.age > bob.age:
#      print(alice.name,alice.age)
# else:
#     print(bob.name,bob.age) 
############################

# Exercise 2 (Folder 9 ex_2.py)
# 1. Write a class called Student with the attributes name (str) and
# studyProgram (str)
# 2. Create three instances. One for yourself, one for your left neighbour and one
# for our right neighbour.
# 3. Add a method printInfo that prints the name and studyProgram of a
# Student. Test your method on the objects!
# 4. Modify the code and add age and gender to the attributes. Modify your
# printing methods respectively too.


class Student:
    def __init__(self, name: str, studyProgram :str, age: int, gender: str  ) -> None:
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender
    
    def printIn(self):
        print(f" NOME:{self.name}: PROGRAMMA: {self.studyProgram} ETA: {self.age} GENERE: {self.gender}")

me = Student("Nicola", "Cloud",20, "M")
le = Student("Davide", "Cloud",34,"M")
re = Student("Mauro", "Cloud",45,"F")


me.printIn()
le.printIn()
re.printIn()


# Exercise 3 (Folder 9 ex_3.py)
# Given is the class Animal. For each task, test your changes!
# 1. Create two realistic instances of Animals
# 2. Print the name of each object
# 3. Change the amount of legs of one object using the dot notation
# 4. Add a method setLegs() to set the legs of an object and repeat task 3 but
# this time using the method.
# 5. Add a method getLegs() to return the amount of legs
# 6. Add a method named printInfo that prints all attributes of the Animal


# class Animal:
#     def _init_ (self, name: str, legs:str):
#         self.name = name
#         self.legs =legs

#     def get_legs (self):
#         return self.legs
    
#     def set_legs (self, x:int):
        

#     # def __str__(self) -> str:
    
#     #     pass


# Exercise 4 (Folder 9 ex_4.py)
# 1. Write a new class called Food, it should have name, price and
# description as attributes.
# 2. Instantiate at least three different foods you know and like.
# 3. Create a new class called Menu, it should have a list (of Foods) as attribute.
# __init__ should take a list of Foods as optional parameters (default=[])
# 4. Create a addFood() and removeFood() for the Menu
# 5. Create a few new Food instances. Add each to the Menu using the respective
# Method.
# 6. Add a method printPrices() that list all items on the Menu with their
# prices.
# 7. Add a Menu method getAveragePrice() that returns the average Food
# price of the Men


class Food:

    def _init_  (self, name: str, price: int, descr:str ):
        self.name = name 
        self.price = price 
        self.descr = descr


pecorino = Food("Pecorino",3, "formaggio")
pizza = Food ("pizza",6, "farina e acqua")
Tonno = Food ("Tonno",14, "pesce")

class Menu:

    def _init_ (self,lista:list[Food]=[]):
        self.lista= lista

    def addFood(self, AddFood):
        AddFood
        
        

    
