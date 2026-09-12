import math

from calculations.probability import Summations, HyperGeometricDistribution, NegativeHyperGeometricDistribution

print("-----------------------------------------------------------------------------------------------------")
print("This document will outline all numeric values of Customers with an intentful E.V. to Variance curve")
print("-----------------------------------------------------------------------------------------------------")

print("-----------------------------------------------------------------------------------------------------")
print("What’s the average amount of Customer Tokens pulled before End of Round?")
print("(10 basic customers per player, 4 EoR tokens per player)")
# print("The round ends whenever ALL EoR tokens have been pulled from ALL player's bags")
# print("Therefore, the question is: on average, how many tokens will an individual player get to pull before all 3/6/9/12 EoR tokens are pulled?")
print("-----------------------------------------------------------------------------------------------------")

avg_pulls_1p = NegativeHyperGeometricDistribution.expected_value(13,3,3)
print("Avg tokens pulled for 1 player: " + str(avg_pulls_1p))

variance_1p = NegativeHyperGeometricDistribution.variance(13,3,3)

standard_deviation_1p = math.sqrt(variance_1p)
coefficient_of_variation_1p = standard_deviation_1p / avg_pulls_1p

print("Avg std deviation for 1 player: " + str(standard_deviation_1p))
print("Coefficient of variation std deviation for 1 player: " + str(coefficient_of_variation_1p))
print("-----------------------------------------------------------------------------------------------------")
print("Now what should the tokens per customer category be?")
print("-----------------------------------------------------------------------------------------------------")
print("Setting variables")
print("-----------------------------------------------------------------------------------------------------")
#List of monetary offers

kitchen_k_set = [2, 2] # 4 - 1 * 2 = 2
kitchen_items = [0,1,2,0,1,2,1,1,1,2,1]

clothes_k_set = [2, 3] # 5 - 1.5 * 2 = 2
clothes_items = [1,1,2,1,1,2,1,1,1,2,1]

art_k_set = [2, 4] # 7 - 1.5 * 2 = 3
art_items = [2,2,2,2,1,2,1]

electronics_k_set = [3, 4] # 7 - 2 * 2 = 3
electronics_items = [2,2,2,2,2,2,2]

furniture_k_set = [4,5] # 9 - 3 * 2 = 3
furniture_items = [3,2,3,2,3]

end_of_round_tokens = [0,0,0]
total_set = kitchen_k_set + clothes_k_set + electronics_k_set + art_k_set + furniture_k_set + end_of_round_tokens

customer_bag = {
    "kitchen": {
        "k_set": kitchen_k_set,
        "avg_cost": Summations.get_arithmetic_mean(kitchen_items) # price to purchase before selling phase
    },
    "clothes": {
        "k_set": clothes_k_set,
        "avg_cost": Summations.get_arithmetic_mean(clothes_items)
    },  
    "electronics": {
        "k_set": electronics_k_set,
        "avg_cost": Summations.get_arithmetic_mean(electronics_items)
    },
    "art": {
        "k_set": art_k_set,
        "avg_cost": Summations.get_arithmetic_mean(art_items)
    },
    "furniture": {
        "k_set": furniture_k_set,
        "avg_cost": Summations.get_arithmetic_mean(furniture_items)
    },
    "end_of_round": {
        "k_set": end_of_round_tokens,
    },
    "total_set": {
        "k_set": kitchen_k_set + clothes_k_set + electronics_k_set + art_k_set + furniture_k_set + end_of_round_tokens
    }
}

game_plots = {
    "plots": [],
    "ideal_x": [1, 2, 3, 4, 5, 6],
    "ideal_y": [0.5, 1, 1.5, 2, 2.5, 3 ]
}



print("-----------------------------------------------------------------------------------------------------")
print("running calculations")
print("-----------------------------------------------------------------------------------------------------")
for category_type, category in customer_bag.items():
    if category_type not in ["end_of_round", "total_set"]:
        # setting commonly used variables
        population_n = len(customer_bag["total_set"]["k_set"]) - 3
        # not 13, it's 9 because we're ignoring the 4 EoR tokens

        non_end_of_round_tokens_pulled = math.floor(avg_pulls_1p - 3)
        # not 9, it's 6 tokens because this is how many customers you are expected to pull with no bag manipulation

        k_collection = category["k_set"]

        # exa. a monetary offer of [10, 11] is very good
        # However, if the avg cost of that category of item is 10 then it's basically [0,1]
        k_as_proft = list (customer - category["avg_cost"] for customer in category["k_set"] if category["k_set"] == k_collection)

        # revenue calculations
        ev = Summations.get_total_expectation(population_n,k_as_proft, non_end_of_round_tokens_pulled)
        total_variance = Summations.get_total_variance(population_n,k_as_proft, non_end_of_round_tokens_pulled)
        standard_deviation = math.sqrt(total_variance)
        coefficient_variation = standard_deviation / ev

        # profit calculations
        average_expenses = HyperGeometricDistribution.expected_value(population_n,non_end_of_round_tokens_pulled,len(k_collection)) * category["avg_cost"]
        ev_profit = ev - average_expenses

        print(category_type + " ev: " + str(ev))
        print(category_type + " standard deviation: " + str(standard_deviation))
        print(category_type + " coefficient variation: " + str(coefficient_variation))
        print(category_type + " average expenses: " + str(average_expenses))
        print("-----------------------------------------------------------------------------------------------------")
        plot = {
            "label": category_type,
            "x": ev,
            "y": standard_deviation,
            "y2": average_expenses,
        }
        game_plots["plots"].append(plot)



import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Matplotlib View")

        canvas = MatplotlibCanvas(self, width=5, height=4, dpi=100)
        canvas.axes.set_xlabel("Expected profit")
        canvas.axes.set_ylabel("Standard Deviation")

        canvas.axes.plot(game_plots["ideal_x"], game_plots["ideal_y"], color="blue", linewidth=2)
        for game_plot in game_plots["plots"]:
            canvas.axes.annotate(game_plot["label"], (game_plot["x"], game_plot["y"]), xytext=(10,10), textcoords='offset points')
            canvas.axes.scatter(game_plot["x"], game_plot["y"], label=game_plot["label"], color="red", linewidth=2)


        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

