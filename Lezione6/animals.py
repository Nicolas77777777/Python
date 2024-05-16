from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age) -> None:
        super().__init__()

        self.name= name
        self.age= age 


@abstractmethod
def verso():
    pass



class Cat(Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)

    def verso ():
        print("Miao")

class Dog(Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)

    def verso (self):
            print()