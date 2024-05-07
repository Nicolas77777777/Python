# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


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


class Animal:
    def _init_ (self, name: str, legs:str):
        self.name = name
        self.legs =legs

    def get_legs (self):
        return self.legs
    
    def set_legs (self, x:int):
        

    def __str__(self) -> str:
        pass













        

