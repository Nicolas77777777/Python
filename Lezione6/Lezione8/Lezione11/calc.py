i : int = 1
assert 1 == 0, f" The value must be equal to 0 instead is {i}"


# def check_sqrt(func, input, result) :
#     n = func(input)
#     pass

#     assert n == result, f"Error the expected value"

class Calcutations:
    def __init__(self, a: float, b:float) -> None:
        self.a : float = a
        self.b : float = b

    def get_sum (self):

        return self.a + self.b
    
    def get_difference(self):

        return self.a - self.b
    
    def get_product(self):

        return self.a * self.b
    

    def divisione(self):

        return self.a / self.b
    

    

