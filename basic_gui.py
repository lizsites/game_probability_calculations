import tkinter as tk
from tkinter import messagebox
from calculations.probability import Summations
import logging

logging.basicConfig(
    level=logging.ERROR
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
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

k_label = tk.Label(root, text="How many successes do you want?", font=("Arial", 14))
k_label.pack(pady=10)

# Create the Entry widget for single-line input
k_field = tk.Entry(root, width=25, textvariable=default_k)
k_field.pack(pady=10)

def show_message(items: list):
    for item in items:
        messagebox.showinfo(item["title"], item["message"])


def compare_probabilities():
    population_n = int(population_n_field.get())
    population_k = int(population_k_field.get())
    n = int(n_field.get())
    k = int(k_field.get())

    logger.debug(f"Population N: {str(population_n)}")
    logger.debug(f"Population K: {str(population_k)}")
    logger.debug(f"n: {str(n)}")
    logger.debug(f"k: {str(k)}")
    hyper_geometric_sum = Summations.hyper_geometric_pmf(population_n, population_k, n, k)
    logger.debug(f"chances by basic hyper geometric sum: {str(hyper_geometric_sum)}")
    comparison_message = dict(
        title="measured hyper geometrically",
        message=f"measured hyper geometrically: {str(hyper_geometric_sum)}")
    show_message([comparison_message])


button = tk.Button(root, text="Submit", command=compare_probabilities, bg="blue", fg="white")
button.pack(pady=10)


# Run the background application loop
root.mainloop()