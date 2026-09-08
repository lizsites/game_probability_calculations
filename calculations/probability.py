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
    def expected_value(population_n: int, population_k: int, k: int):
        return ((population_n + 1) / (population_k + 1)) * k

    @staticmethod
    def variance(population_n: int, population_k: int, k: int):
        numerator = population_k * (population_n + 1) * (population_n - population_k) * (population_k + 1 - k)
        denominator = ((population_k + 1) ** 2 * ( population_k + 2))
        # numerator = (population_k * (population_n + 1) * (population_n - population_k - x + 1))
        # denominator = ((population_n - population_k + 1) ** 2 * (population_n - population_k + 2))
        return numerator / denominator



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
    def negative_hyper_geometric_summed_pmf(population_n: int, population_k: int, x: int, k: int):
        weighted_value = 0
        n=k
        while n <= x:
            weighted_value = weighted_value + NegativeHyperGeometricDistribution.pmf(population_n, population_k, n, k)
            n = n + 1
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
    def get_total_variance(population_n: int, k_list: list, n: int):
        variance = 0
        population_k = len(k_list)
        expected_value = Summations.get_total_expectation(population_n, k_list, n)
        power_collection = Summations.get_power_collection(k_list)
        for k, subsets in power_collection.items():
            # 0, 1, 2, 3 (targeted number of successes)
            for subset in subsets:
                v_sum = sum(subset)
                # population_n: 27
                # population_n: 3
                # n: 13
                # k: provided by for loop (0, 1,2,3)
                variance = variance + HyperGeometricDistribution.pmf(population_n, population_k, n, k) * (1/len(subsets)) * (v_sum - expected_value)**2
        return variance

    @staticmethod
    def get_power_collection(k_set: list):
        # it makes a tuple of elements like this format
        # element 1 - 10
        # element 2 - 12
        # element 3 - 14

        # 10, 10, 18, 12
        k_labelled = tuple("element " + str(k_index) + " -" + str(item) for k_index, item in enumerate(k_set))
        power_collection = Summations.get_raw_power_collection({}, k_labelled)
        return Summations.clean_raw_power_collection(power_collection)

    @staticmethod
    def get_raw_power_collection(power_collection: dict, k_set: tuple):

        # assume you have a collection consisting of {1,2,3}
        #{
        #   0 : [()],
        #   1 : [(1), (2), (3)],
        #   2 : [(1,2), (2,3), (1,3)],
        #   3 : [(1,2,3)]
        # }
        if len(k_set) not in power_collection:
            power_collection[len(k_set)] = set()
        power_collection[len(k_set)].add(k_set)
        for k_index, k in enumerate(k_set):
            filtered_tuple = tuple(k_set[:k_index] + k_set[k_index + 1:])
            power_collection = Summations.get_raw_power_collection(power_collection, filtered_tuple)
        return power_collection

    @staticmethod
    def clean_raw_power_collection(power_collection: dict):
        power_collection_cleaned = {}
        for (element_count, unique_elements) in power_collection.items():
            cleaned_combinations = []
            for element_combination in unique_elements:
                cleaned_list = list()
                for element in element_combination:
                    cleaned_element = element.split("-")
                    cleaned_list.append(float(cleaned_element[1]))
                cleaned_combinations.append(list(cleaned_list))
            power_collection_cleaned[element_count] = cleaned_combinations
        return power_collection_cleaned