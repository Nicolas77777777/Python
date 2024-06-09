from abc import ABC, abstractmethod

"""" Create an abstract class Shape with an abstract method area 
and another abstract method perimeter. Then, create two subclasses
 Circle and Rectangle that implement the area and perimeter methods."""

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
    
    def perimeter (self,radius: float):
        perimeter= (2*3.14)*radius
        return f'circle perimeter = {perimeter}'
    
class Rectangle(Shape):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def area (self, base: float, height:float):
        area= base * height
        return f'rectangle area = {area}'
    
    def perimeter (self, base: float, height:float):
        perimeter= (2*base)+ (2*height)
        return f'rectangle perimeter = {perimeter}'
    
   
ce:Circle = Circle("circle")
re: Rectangle = Rectangle("rectangle")

ce.area(5)
ce.perimeter(7)

re.area(20,18)
re.perimeter(5,5)


"""" Exercise 2: Implementing Static Methods

Create a class MathOperations with a static method add 
that takes two numbers and returns their sum, and another 
static method multiply  that takes two numbers and returns their product."""

class MathOperations:
    def __init__(self) :
         pass
         


    @staticmethod
    def sum(num_a: float, num_b: float):
            resul= num_a + num_b
            return resul
        

    @staticmethod
    def multiply(num_a: float, num_b: float):
            resul = num_a * num_b
            return resul
  

s= MathOperations.sum(11,22)
#librery Biblioteca 


"""" titolo autore e isbn """

# creare una istanza da una stringa

# utilizzare split sulla virgola titolo autore e isbn 

# 
