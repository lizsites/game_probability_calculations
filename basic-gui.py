import tkinter as tk
from tkinter import messagebox
import gagnon_senseis_method
from calculations.prob_utilities import distributions, summations

# Initialize the main system window
root = tk.Tk()

default_N = tk.IntVar(value=30)
default_K = tk.IntVar(value=3)
default_n = tk.IntVar(value=15)
default_k = tk.IntVar(value=2)

root.title("Input the round you want to check End probabilities for this game")
root.geometry("700x400")

N_label = tk.Label(root, text="How many items are there?", font=("Arial", 14))
N_label.pack(pady=10)


# Create the Entry widget for single-line input
N_field = tk.Entry(root, width=25, textvariable=default_N)
N_field.pack(pady=10)

K_label = tk.Label(root, text="How many items would you consider a success?", font=("Arial", 14))
K_label.pack(pady=10)

# Create the Entry widget for single-line input
K_field = tk.Entry(root, width=25, textvariable=default_K)
K_field.pack(pady=10)

n_label = tk.Label(root, text="How many trials will you have?", font=("Arial", 14))
n_label.pack(pady=10)

# Create the Entry widget for single-line input
n_field = tk.Entry(root, width=25, textvariable=default_n)
n_field.pack(pady=10)

def show_message(items: list):
    for item in items:
        messagebox.showinfo(item["title"], item["message"])


def compare_probalitities():
    N = int(N_field.get())
    K = int(K_field.get())
    n = int(n_field.get())
    print(N)
    print(K)
    print(n)
    push_your_luck_chances = gagnon_senseis_method.push_your_luck_style(N, K, n, 2)
    hyper_geometric_sum = summations.get_sum(N, K, n, 2)
    print("gagnon's method: " + str(push_your_luck_chances))
    print("hyper-geometric sum: " + str(hyper_geometric_sum))
    push_your_luck_message = dict(title="Gagnon Sensei's Method", message=str(push_your_luck_chances))
    hyper_geometric_message = dict(title="measured hyper geometrically", message=str(str(hyper_geometric_sum)))
    show_message([push_your_luck_message, hyper_geometric_message])




button = tk.Button(root, text="Submit", command=compare_probalitities, bg="blue", fg="white")
button.pack(pady=10)




# Run the background application loop
root.mainloop()



# print(gagnon_senseis_method.get_round_end_chance_by_this_pull(30, 3, 15, 2))
# print(distributions.get_hyper_geometric_chances(30, 3, 15, 2) + distributions.get_hyper_geometric_chances(30, 3, 15, 3))