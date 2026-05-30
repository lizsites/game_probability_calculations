import unittest
import random
from prob_utilities import distributions

class test_distributions(unittest.TestCase):
    
    def test_hyper_geometric(self):
        sum_of_chances = 0
        N = random.randint(1,100)
        n = random.randint(1, N)
        K = random.randint(1, N)
        k = 0

        # we need to avoid situations that are impossible like having more successful events and amount of trials
        # without eliminating the possibility of having more possible successes than trials
        while (K + n) > N:
            n=random.randint(1, N)
            K=random.randint(1, N)

        print("total_events_size: " + str(N))
        print("amount_of_trials: " + str(n))
        print("total_successful_events_size: " + str(K))
        print("target_successful_trials: " + str(k))
        while  k <= K and k <= n:
            sum_of_chances = sum_of_chances + distributions.get_hyper_geometric_chances(N, K, n, k)
            k = k + 1
            print("sum_of_chances: " + str(sum_of_chances))
            print("target_successful_trials: " + str(k))

        self.assertTrue(1.001 > sum_of_chances and sum_of_chances > 0.999999)
    
    def test_0_hyper_geometric(self):
        sum_of_chances = 0
        N = 0
        n = 0
        K = 0
        k = 0

        print("total_events_size: " + str(N))
        print("amount_of_trials: " + str(n))
        print("total_successful_events_size: " + str(K))
        print("target_successful_trials: " + str(k))
        while  k <= K and k <= n:
            sum_of_chances = sum_of_chances + distributions.get_hyper_geometric_chances(N, K, n, k)
            k = k + 1
            print("sum_of_chances: " + str(sum_of_chances))
            print("target_successful_trials: " + str(k))

        self.assertTrue(1.001 > sum_of_chances and sum_of_chances > 0.999999)


        
    def test_binomial(self):
        sum_of_chances = 0
        p=random.random()
        N = random.randint(1,100)
        n = random.randint(1, N)
        k = 0

        print("amount_of_trials: " + str(n))
        print("target_successful_trials: " + str(k))
        while k <= n:
            sum_of_chances = sum_of_chances + distributions.get_binomial_chances(n, k, p)
            k = k + 1
            print("sum_of_chances: " + str(sum_of_chances))
            print("target_successful_trials: " + str(k))

        self.assertTrue(1.001 > sum_of_chances and sum_of_chances > 0.999999)

if __name__ == '__main__':
    unittest.main()