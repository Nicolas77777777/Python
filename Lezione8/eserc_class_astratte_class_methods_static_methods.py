from abc import ABC, abstractmethod

"""" Create an abstract class Shape with an abstract method area 
and another abstract method perimeter. Then, create two subclasses
 Circle and Rectangle that implement the area and perimeter methods.
 
 Crea una classe astratta Shape con un'area del metodo astratto e un altro 
 perimetro del metodo astratto. Quindi, crea due sottoclassi
Circle e Rectangle che implementano i metodi area e perimetro.
 """

class Shape(ABC):
    def __init__(self, name : str) -> None:
        super().__init__()

        self.name = name

@abstractmethod
def area (self):
    pass

@abstractmethod
def perimeter (self):
    pass

class Circle(Shape):

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def area (self,radius:float):
        area= 3.14 *(radius**2)
        return f'circle area = {area}'
    
    def perimeter (self,radius):
        perimeter= (2*3.14)*radius
        return f'circle perimeter= {perimeter}'
    
ce:Circle= Circle("cerchio")

print(ce.area(5))




"""" Exercise 2: Implementing Static Methods

Create a class MathOperations with a static method add 
that takes two numbers and returns their sum, and another 
static method multiply  that takes two numbers and returns their product."""

#librery Biblioteca 


"""" titolo autore e isbn """

# creare una istanza da una stringa

# utilizzare split sulla virgola titolo autore e isbn 

# 
