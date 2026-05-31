import unittest
import random
from calculations.prob_utilities import Distributions,Summations

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

        sum_of_chances = Summations.get_hyper_geometric_sum(population_n, population_k, n, k)

        self.assertTrue(1.001 > sum_of_chances > 0.999999)
    
    def test_0_hyper_geometric(self):
        population_n = 0
        n = 0
        population_k = 0
        k = 0

        sum_of_chances = Summations.get_hyper_geometric_sum(population_n, population_k, n, k)

        self.assertTrue(1.001 > sum_of_chances > 0.999999)


        
    def test_binomial(self):
        sum_of_chances = 0
        p=random.random()
        population_n = random.randint(1,100)
        n = random.randint(1, population_n)
        k = 0

        print("amount_of_trials: " + str(n))
        print("target_successful_trials: " + str(k))
        while k <= n:
            sum_of_chances = sum_of_chances + Distributions.get_binomial_chances(n, k, p)
            k = k + 1
            print("sum_of_chances: " + str(sum_of_chances))
            print("target_successful_trials: " + str(k))

        self.assertTrue(1.001 > sum_of_chances > 0.999999)

if __name__ == '__main__':
    unittest.main()