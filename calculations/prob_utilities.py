import math
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

class Distributions:
    @staticmethod
    def permutation_formula(collection_size: int, sample_size: int):
        permutations = 0
        try:
            if sample_size > collection_size:
                raise ValueError("Sample size must be less than / equal to collection size")
            permutations = math.factorial(collection_size)/(math.factorial(collection_size - sample_size))
        except ValueError:
            logger.debug("collection_size: " + str(collection_size))
            logger.debug("sample_size: " + str(sample_size))
        return permutations


    @staticmethod
    def combination_formula(collection_size: int, sample_size: int):
        return Distributions.permutation_formula(collection_size, sample_size) / math.factorial(sample_size)

    @staticmethod
    def get_hyper_geometric_chances(population_n: int, population_k: int, n: int, k: int):
        pop_k_choose_k = Distributions.combination_formula(population_k, k)
        pop_nk_choose_nk = Distributions.combination_formula(population_n - population_k, n - k)
        pop_n_choose_n = Distributions.combination_formula(population_n, n)
        return (pop_k_choose_k * pop_nk_choose_nk) / pop_n_choose_n

    @staticmethod
    def get_geometric_chances(p: float):
        return 1/p

    @staticmethod
    def get_binomial_chances(n: int, x: int, p: float):
        n_choose_x = Distributions.combination_formula(n,x)
        return n_choose_x * p**x * (1-p)**(n-x)

    @staticmethod
    def get_singular_event_chance(total_successful_events_size: int, total_events_size: int):
        return total_successful_events_size/total_events_size


class Summations:
    @staticmethod
    def get_hyper_geometric_sum(population_n: int, population_k: int, n: int, k: int):
        sum_of_chances = 0
        while k <= population_k  and k <= n:
            sum_of_chances = sum_of_chances + Distributions.get_hyper_geometric_chances(population_n, population_k, n, k)
            k = k + 1
        return sum_of_chances
