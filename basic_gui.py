import tkinter as tk
from tkinter import messagebox
import gagnon_senseis_method
from calculations.prob_utilities import Summations
import logging

logging.basicConfig(
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Initialize the main system window
root = tk.Tk()

default_population_n = tk.IntVar(value=30)
default_population_k = tk.IntVar(value=3)
default_n = tk.IntVar(value=15)
default_k = tk.IntVar(value=2)

root.title("Input the round you want to check End probabilities for this game")
root.geometry("700x400")

population_n_label = tk.Label(root, text="How many items are there?", font=("Arial", 14))
population_n_label.pack(pady=10)


# Create the Entry widget for single-line input
population_n_field = tk.Entry(root, width=25, textvariable=default_population_n)
population_n_field.pack(pady=10)

population_k_label = tk.Label(root, text="How many items would you consider a success?", font=("Arial", 14))
population_k_label.pack(pady=10)

# Create the Entry widget for single-line input
population_k_field = tk.Entry(root, width=25, textvariable=default_population_k)
population_k_field.pack(pady=10)

n_label = tk.Label(root, text="How many trials will you have?", font=("Arial", 14))
n_label.pack(pady=10)

# Create the Entry widget for single-line input
n_field = tk.Entry(root, width=25, textvariable=default_n)
n_field.pack(pady=10)

def show_message(items: list):
    for item in items:
        messagebox.showinfo(item["title"], item["message"])


def compare_probabilities():
    population_n = int(population_n_field.get())
    population_k = int(population_k_field.get())

    n = int(n_field.get())
    logger.debug(f"Population N: {str(population_n)}")
    logger.debug(f"Population K: {str(population_k)}")
    logger.debug(f"n: {str(n)}")
    logger.debug(f"k: hard-coded to 2 for this example")
    push_your_luck_chances = gagnon_senseis_method.push_your_luck_style(population_n, population_k, n, 2)
    logger.debug(f"chances by push-your-luck logic: {str(push_your_luck_chances)}")
    hyper_geometric_sum = Summations.get_hyper_geometric_sum(population_n, population_k, n, 2)
    logger.debug(f"chances by basic hyper geometric sum: {str(hyper_geometric_sum)}")
    comparison_message = dict(
        title="Gagnon Sensei's Method",
        message=f"Gagnon Sensei's Method: {str(push_your_luck_chances)}\nmeasured hyper geometrically: {str(hyper_geometric_sum)}")
    show_message([comparison_message])


button = tk.Button(root, text="Submit", command=compare_probabilities, bg="blue", fg="white")
button.pack(pady=10)


# Run the background application loop
root.mainloop()