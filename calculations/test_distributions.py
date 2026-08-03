import unittest
import random
from calculations.probability import Summations

class Test_Distributions(unittest.TestCase):
    
    def test_hyper_geometric(self):
        sum_of_chances = 0
        population_n = random.randint(1,100)
        n = random.randint(1, population_n)
        population_k = random.randint(1, population_n)
        k = 0

        # we need to avoid situations that are impossible like having more successful events and amount of trials
        # without eliminating the possibility of having more possible successes than trials
        while (population_k + n) > population_n:
            n=random.randint(1, population_n)
            population_k=random.randint(1, population_n)

        sum_of_chances = Summations.hyper_geometric_pmf(population_n, population_k, n, k)

        self.assertTrue(1.001 > sum_of_chances > 0.999999)
    
    def test_0_hyper_geometric(self):
        population_n = 0
        n = 0
        population_k = 0
        k = 0

        sum_of_chances = Summations.hyper_geometric_pmf(population_n, population_k, n, k)

        self.assertTrue(1.001 > sum_of_chances > 0.999999)


        
    def test_binomial(self):
        n = random.randint(1,100)
        x = random.randint(1, n)
        p=random.random()

        sum_of_chances = Summations.binomial_pmf(n, x, p)
        self.assertTrue(1.001 > sum_of_chances > 0.999999)

    def test_binomial_zero(self):
        n = 0
        x = 0
        p=0

        sum_of_chances = Summations.binomial_pmf(n, x, p)
        self.assertTrue(1.001 > sum_of_chances > 0.999999)


if __name__ == '__main__':
    unittest.main()