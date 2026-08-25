import math

from calculations.probability import Summations, BinomialDistribution, HyperGeometricDistribution

print("-----------------------------------------------------------------------------------------------------")
print("OLD VERSION (v1)")
print("summarized: 27 starting customers, un-even tile distribution by type")
print("-----------------------------------------------------------------------------------------------------")

print("Expected Value of Monetary Offers for Furniture Customers (v1): " + str(
    Summations.get_total_expectation(27, [8, 18, 25], 13)))
print("Expected Value of Monetary Offers for Art Customers (v1): " + str(
    Summations.get_total_expectation(27, [4, 9, 14, 20], 13)))
print("Expected Value of Monetary Offers for Electronics Customers (v1): " + str(
    Summations.get_total_expectation(27, [5, 9, 13, 18], 13)))
print("Expected Value of Monetary Offers for Clothes Customers (v1): " + str(
    Summations.get_total_expectation(27, [1, 3, 5, 7, 10], 13)))
print("Expected Value of Monetary Offers for Kitchen Customers (v1): " + str(
    Summations.get_total_expectation(27, [2, 3, 4, 5, 7], 13)))

print("-----------------------------------------------------------------------------------------------------")
print("REVISED VERSION (v2)")
print("summarized: 10 starting customers, 2 starting customers per type, no vibe customers")
print("-----------------------------------------------------------------------------------------------------")

furniture_ev_v2 = Summations.get_total_expectation(10, [10, 14], 7)
art_ev_v2 = Summations.get_total_expectation(10, [5, 10], 7)
electronics_ev_v2 = Summations.get_total_expectation(10, [6, 9], 7)
clothes_ev_v2 = Summations.get_total_expectation(10, [3, 8], 7)
kitchen_ev_v2 = Summations.get_total_expectation(10, [4, 7], 7)

furniture_avg_cost = Summations.get_arithmetic_mean([11, 11, 11, 11, 12, 15])
art_avg_cost = Summations.get_arithmetic_mean([6, 6, 5 ,6, 7])
electronics_avg_cost = Summations.get_arithmetic_mean([6, 6, 5, 6, 7, 7, 7, 8, 10])
clothes_avg_cost = Summations.get_arithmetic_mean([3, 4, 3, 5, 4, 4, 4, 3, 3, 3, 3])
kitchen_avg_cost = Summations.get_arithmetic_mean([2, 3, 2, 2, 3, 3, 3, 6, 3, 3, 4])

print("Expected Value of Monetary Offers for Furniture Customers (v2): " + str(
    furniture_ev_v2) + " - " + str(furniture_avg_cost) + " = " +  str(furniture_ev_v2 - furniture_avg_cost))
print("Expected Value of Monetary Offers for Art Customers (v2): " + str(
    art_ev_v2) + " - " + str(art_avg_cost) + " = " +  str(art_ev_v2 - art_avg_cost))
print("Expected Value of Monetary Offers for Electronics Customers (v2): " + str(
    electronics_ev_v2) + " - " + str(electronics_avg_cost) + " = " +  str(electronics_ev_v2 - electronics_avg_cost))
print("Expected Value of Monetary Offers for Clothes Customers (v2): " + str(
    clothes_ev_v2) + " - " + str(clothes_avg_cost) + " = " +  str(clothes_ev_v2 - clothes_avg_cost))
print("Expected Value of Monetary Offers for Kitchen Customers (v2): " + str(
    kitchen_ev_v2) + " - " + str(kitchen_avg_cost) + " = " +  str(kitchen_ev_v2 - kitchen_avg_cost))



print("-----------------------------------------------------------------------------------------------------")
print("Just lesson notes")
print("-----------------------------------------------------------------------------------------------------")
print("expected value of old furniture distribution: " + str(Summations.hyper_geometric_expected_value(27,2,13)))
print("variance of old furniture distribution: " + str(Summations.hyper_geometric_variance(27,2,13)))
print("coefficient of variation of old furniture distribution: " + str(Summations.hyper_geometric_coefficient_of_variation(27,2,13)))


print("-----------------------------------------------------------------------------------------------------")
print("compare by adding 1 more furniture customer")
print("-----------------------------------------------------------------------------------------------------")
print("expected value of new furniture distribution: " + str(Summations.hyper_geometric_expected_value(27,3,13)))
print("variance of new furniture distribution: " + str(Summations.hyper_geometric_variance(27,3,13)))
print("coefficient of variation of new furniture distribution: " + str(Summations.hyper_geometric_coefficient_of_variation(27,3,13)))



print("-----------------------------------------------------------------------------------------------------")
print("Hand calculating Variance for one type")
print("-----------------------------------------------------------------------------------------------------")

# 10 and 14 as monetary offers

furniture_chances_of_drawing_1 = HyperGeometricDistribution.pmf(10, 2, 7, 1)
furniture_chances_of_drawing_2 = HyperGeometricDistribution.pmf(10, 2, 7, 2)


print("Chances of drawing 1 Furniture Customer: " + str(
    furniture_chances_of_drawing_1))

print("Chances of drawing 2 Furniture Customers: " + str(
    furniture_chances_of_drawing_2))

variance_by_hand = furniture_chances_of_drawing_1 * 0.5 * (10 - furniture_ev_v2)**2 + furniture_chances_of_drawing_1 * 0.5 * (14 - furniture_ev_v2)**2 + furniture_chances_of_drawing_2 * (10 + 14 - furniture_ev_v2)**2

print("Variance by hand: " + str(variance_by_hand))
print("Standard deviation by hand: " + str(math.sqrt(variance_by_hand)))
print("Coefficient of variation by hand: " + str(math.sqrt(variance_by_hand)/furniture_ev_v2))

print("-----------------------------------------------------------------------------------------------------")
print("Getting power set")
print("-----------------------------------------------------------------------------------------------------")
power_set = Summations.get_power_set([10,12,14,16])

print(power_set)

# furniture_var_v2 = Summations.get_total_variance(10, [10, 14], 7)
# art_var_v2 = Summations.get_total_variance(10, [5, 10], 7)
# electronics_var_v2 = Summations.get_total_variance(10, [6, 9], 7)
# clothes_var_v2 = Summations.get_total_variance(10, [3, 8], 7)
# kitchen_var_v2 = Summations.get_total_variance(10, [4, 7], 7)



# print("Variance of Monetary Offers for Furniture Customers (v2): " + str(furniture_var_v2))
# print("Variance of Monetary Offers for Art Customers (v2): " + str(
#     art_var_v2))
# print("Variance of Monetary Offers for Electronics Customers (v2): " + str(
#     electronics_var_v2))
# print("Variance of Monetary Offers for Clothes Customers (v2): " + str(
#     clothes_var_v2))
# print("Variance of Monetary Offers for Kitchen Customers (v2): " + str(
#     kitchen_var_v2))
