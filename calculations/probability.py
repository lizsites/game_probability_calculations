import math
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

class Formulas:
    @staticmethod
    def permutation_formula(collection_size: int, sample_size: int):
        permutations = 0
        try:
            if sample_size > collection_size:
                raise ValueError("Sample size must be less than / equal to collection size")
            permutations = math.factorial(collection_size)/(math.factorial(collection_size - sample_size))
        except ValueError as e:
            logger.error(e)
            logger.error("collection_size: " + str(collection_size))
            logger.error("sample_size: " + str(sample_size))
        return permutations


    @staticmethod
    def combination_formula(collection_size: int, sample_size: int):
        return Formulas.permutation_formula(collection_size, sample_size) / math.factorial(sample_size)

class BinomialDistribution:
    @staticmethod
    def pmf(n: int, x: int, p: float):
        n_choose_x = Formulas.combination_formula(n,x)
        return n_choose_x * p**x * (1-p)**(n-x)

    @staticmethod
    def expected_value(n: int, p: float):
        return n*p

    @staticmethod
    def variance(n: int, p: float):
        return n * p * (1 - p)

class GeometricDistribution:
    @staticmethod
    def pmf(x: int, p: float):
        return ((1 - p) ** (x - 1)) * p

    @staticmethod
    def expected_value(p: float):
        return 1/p

    @staticmethod
    def variance(p: float):
        return (1 - p)/p

class HyperGeometricDistribution:
    @staticmethod
    def pmf(population_n: int, population_k: int, n: int, k: int):
        p = 0
        try:
            if k > n:
                raise ValueError("Invalid, k > n")
            if population_k > population_n:
                raise ValueError("Invalid, pop_k > pop_n")

            pop_k_choose_k = Formulas.combination_formula(population_k, k)
            pop_nk_choose_nk = Formulas.combination_formula(population_n - population_k, n - k)
            pop_n_choose_n = Formulas.combination_formula(population_n, n)
            p = (pop_k_choose_k * pop_nk_choose_nk) / pop_n_choose_n
        except ValueError as e:
            logger.debug(e)
        return p

    @staticmethod
    def expected_value(population_n: int, n: int, k: int):
        return (n*k)/population_n

    @staticmethod
    def variance(population_n: int, population_k: int, n: int, k: int):
        return n * (population_k / population_n) * ((population_n - population_k) / population_n) * ((population_n - n) / (population_n - 1))



class NegativeHyperGeometricDistribution:
    @staticmethod
    def pmf(population_n: int, population_k: int, x: int, k: int):
        p = 0
        try:
            if k > x:
                raise ValueError("Invalid, k > x")
            if population_k > population_n:
                raise ValueError("Invalid, pop_k > pop_n")
            p = HyperGeometricDistribution.pmf(population_n, population_k, x, k) * (k/x)
        except ValueError as e:
            logger.debug(e)
        return p

    @staticmethod
    def expected_value(population_n: int, population_k: int, x: int):
        return x * population_k / (population_n - population_k + 1)

    @staticmethod
    def variance(population_n: int, population_k: int, x: int):
        numerator = (population_k * (population_n + 1) * (population_n - population_k - x + 1))
        denominator = ((population_n - population_k + 1) ** 2 * (population_n - population_k + 2))
        return x * numerator / denominator



class Summations:
    @staticmethod
    def hyper_geometric_pmf(population_n: int, population_k: int, n: int, k: int):
        sum_of_chances = 0
        while k <= population_k  and k <= n:
            sum_of_chances = sum_of_chances + HyperGeometricDistribution.pmf(population_n, population_k, n, k)
            k = k + 1
        return sum_of_chances

    @staticmethod
    def hyper_geometric_expected_value(population_n: int, population_k: int, n: int):
        weighted_value = 0
        k = 0
        while k <= population_k  and k <= n:
            weighted_value = weighted_value + HyperGeometricDistribution.pmf(population_n, population_k, n, k) * k
            k = k + 1
        return weighted_value


    @staticmethod
    def hyper_geometric_variance(population_n: int, population_k: int, n: int):
        weighted_value = 0
        k = 0
        expected_value = Summations.hyper_geometric_expected_value(population_n, population_k, n)
        while k <= population_k  and k <= n:
            weighted_value = weighted_value + HyperGeometricDistribution.pmf(population_n, population_k, n, k)*(k - expected_value)**2
            k = k + 1
        return weighted_value

    @staticmethod
    def hyper_geometric_coefficient_of_variation(population_n: int, population_k: int, n: int):
        expected_value = Summations.hyper_geometric_expected_value(population_n, population_k, n)
        variance = math.sqrt(Summations.hyper_geometric_variance(population_n, population_k, n))
        return variance / expected_value

    @staticmethod
    def binomial_pmf(n: int, x: int, p: float):
        sum_of_chances = 0
        k = 0
        while k <= n:
            sum_of_chances = sum_of_chances + BinomialDistribution.pmf(n, k, p)
            k = k + 1
        return sum_of_chances

    # This uses the law of total expectations to calculate the summation of V given drawing X amount of tiles
    @staticmethod
    def get_total_expectation(population_n: int, k_set: list, n: int):
        expected_value = 0
        simple_average = Summations.get_arithmetic_mean(k_set)
        population_k = len(k_set)

        for k in range(population_k + 1):
            expected_value = expected_value + HyperGeometricDistribution.pmf(population_n, population_k, n, k) * k * simple_average

        return expected_value

    @staticmethod
    def get_arithmetic_mean(items: list):
        added_total = 0
        number_of_items = len(items)
        for item in items:
            added_total = added_total + item
        return added_total / number_of_items

    @staticmethod
    def get_total_variance(population_n: int, k_set: list, n: int):
        variance = 0
        population_k = len(k_set)
        expected_value = Summations.get_total_expectation(population_n, k_set, n)
        # 10, 12, 14, 16
        # {10, 12, 14, 16}
        # {10, 12, 14}, {10, 14, 16}, {12, 14, 16}
        # {10, 12}, {10, 14}, {10, 16},

        for v in k_set:
            variance = variance + HyperGeometricDistribution.pmf(population_n, population_k, n, 1) * (v - expected_value)**2

        return variance

    @staticmethod
    def get_power_set(k_set: list):
        power_set = Summations.get_power_set_inner({}, tuple(k_set))
        power_set_cleaned = {key: [list(tup) for tup in value] for key, value in power_set.items()}
        return power_set_cleaned

    @staticmethod
    def get_power_set_inner(power_set: dict, k_set: tuple):
        if len(k_set) not in power_set:
            power_set[len(k_set)] = set()
        power_set[len(k_set)].add(k_set)
        for k in k_set:
            filtered_tuple = tuple(item for item in k_set if item != k)
            Summations.get_power_set_inner(power_set, filtered_tuple)
        return power_set