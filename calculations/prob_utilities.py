import math

class distributions:
    def permutation_formula(collection_size: int, sample_size: int):
        return math.factorial(collection_size)/(math.factorial(collection_size - sample_size))

    def combination_formula(collection_size: int, sample_size: int):
        return distributions.permutation_formula(collection_size, sample_size) / math.factorial(sample_size)

    def get_hyper_geometric_chances(N: int, K: int, n: int, k: int):
        K_choose_k = distributions.combination_formula(K, k)
        NK_choose_nk = distributions.combination_formula(N - K, n - k)
        N_choose_n = distributions.combination_formula(N, n)
        return (K_choose_k*NK_choose_nk)/N_choose_n

    def get_geometric_chances(p: float):
        return 1/p

    def get_binomial_chances(n: int, x: int, p: float):
        n_choose_x = distributions.combination_formula(n,x)
        return n_choose_x * p**(x) * (1-p)**(n-x)

    def get_singular_event_chance(total_successful_events_size: int, total_events_size: int):
        return total_successful_events_size/total_events_size


class summations:
    def get_sum(N: int, K: int, n: int, k: int):
        sum_of_chances = 0;
        while k <= K:
            sum_of_chances = sum_of_chances + distributions.get_hyper_geometric_chances(N, K, n, k)
            k = k + 1
        return sum_of_chances
