
from calculations.probability import Summations

print("-----------------------------------------------------------------------------------------------------")
print("OLD VERSION (v1)")
print("summarized: 27 starting customers, un-even tile distribution by type")
print("-----------------------------------------------------------------------------------------------------")

print("Expected Value of Monetary Offers for Furniture Customers (v1): " + str(
    Summations.get_complex_expected_value(27, [12, 18, 25], 13)))
print("Expected Value of Monetary Offers for Art Customers (v1): " + str(
    Summations.get_complex_expected_value(27, [4, 9, 14, 20], 13)))
print("Expected Value of Monetary Offers for Electronics Customers (v1): " + str(
    Summations.get_complex_expected_value(27, [5, 9, 13, 18], 13)))
print("Expected Value of Monetary Offers for Clothes Customers (v1): " + str(
    Summations.get_complex_expected_value(27, [1, 3, 5, 7, 10], 13)))
print("Expected Value of Monetary Offers for Kitchen Customers (v1): " + str(
    Summations.get_complex_expected_value(27, [2, 3, 4, 5, 7], 13)))
print("-----------------------------------------------------------------------------------------------------")
print("REVISED VERSION (v2)")
print("summarized: 10 starting customers, 2 starting customers per type, no vibe customers")
print("-----------------------------------------------------------------------------------------------------")
furniture_ev_v2 = Summations.get_complex_expected_value(10, [10, 15], 7)
art_ev_v2 = Summations.get_complex_expected_value(10, [4, 9], 7)
electronics_ev_v2 = Summations.get_complex_expected_value(10, [6, 10], 7)
clothes_ev_v2 = Summations.get_complex_expected_value(10, [3, 5], 7)
kitchen_ev_v2 = Summations.get_complex_expected_value(10, [3, 4], 7)

furniture_avg_cost = Summations.get_simple_average([11, 11, 11, 11, 12, 15])
art_avg_cost = Summations.get_simple_average([6, 6, 5 ,6, 7])
electronics_avg_cost = Summations.get_simple_average([6, 6, 5, 6, 7, 7, 7, 8, 10])
clothes_avg_cost = Summations.get_simple_average([3, 4, 3, 5, 4, 4, 4, 3, 3, 3, 3])
kitchen_avg_cost = Summations.get_simple_average([2, 3, 2, 2, 3, 3, 3, 6, 3, 3, 4])


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