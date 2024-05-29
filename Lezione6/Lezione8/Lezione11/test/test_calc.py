import unittest

from calc import Calcutations

class TestCalc(unittest.TestCase):

    def test_sum(self):

        calc_1= Calcutations (a=2, b=3)
        result= calc_1.get_sum()


        self.assertEqual(result,5,msg=f'Error Test Failded the goal was 5 the funtion returned{result} ')

        if __name__ == "__main__":
            unittest.main()
