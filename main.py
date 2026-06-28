# import basic_gui
from calculations.probability import Summations
from calculations.probability import BinomialDistribution, GeometricDistribution, HyperGeometricDistribution, NegativeHyperGeometricDistribution

# print(str(Summations.hyper_geometric_expected_value(52,13,2)))
# print(str(Summations.hyper_geometric_expected_value(52,13,3)))
# print(str(Summations.hyper_geometric_expected_value(52,13,4)))
# print(str(Summations.hyper_geometric_expected_value(52,13,5)))



# print(str(BinomialDistribution.pmf(6,2,0.1667)))
# print(str(GeometricDistribution.expected_value(0.4)))
print(str(HyperGeometricDistribution.pmf(28,6,4, 1)))
# print(str(NegativeHyperGeometricDistribution.expected_value(30,3,15)))