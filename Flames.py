import tkinter as tk
import random

def play_flames():
    name1 = entry1.get().strip()
    name2 = entry2.get().strip()

    if not name1 or not name2:
        result_label.config(text="Please enter both names.")
        return

    result = flames(name1, name2)

    if result == "Siblings":
        result_msg = f"Congratulations! {name1} and {name2} are siblings."
    elif result == "Friends":
        result_msg = f"Congratulations! {name1} and {name2} are friends."
    elif result == "Affection":
        result_msg = f"Congratulations! {name1} and {name2} have affection for each other."
    elif result == "Marriage":
        result_msg = f"Congratulations! {name1} and {name2} are meant to be married."
    elif result == "Enemy":
        result_msg = f"Oh no! {name1} and {name2} are enemies."
    elif result == "Love":
        result_msg = f"Congratulations! {name1} and {name2} are in love."

    result_label.config(text=result_msg)

def flames(name1, name2):
    # Convert the names to lowercase and remove spaces
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    # Remove common letters from the names
    for letter in name1:
        if letter in name2:
            name1 = name1.replace(letter, "", 1)
            name2 = name2.replace(letter, "", 1)

    # Calculate the total number of remaining letters
    count = len(name1) + len(name2)

    # Determine the FLAMES result based on the count
    flames_dict = {1: "Siblings", 2: "Friends", 3: "Affection", 4: "Marriage", 5: "Enemy", 6: "Love"}
    keys = list(flames_dict.keys())
    index = 1
    while len(flames_dict) > 1:
        index = (index + count - 1) % len(keys)
        key_to_remove = keys[index]
        keys.remove(key_to_remove)
        del flames_dict[key_to_remove]

    return list(flames_dict.values())[0]

window = tk.Tk()
window.title("FLAMES Game")

label1 = tk.Label(window, text="Enter your name:")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(window)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(window, text="Enter your crush's/lover's name:")
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=10, pady=10)

play_button = tk.Button(window, text="Play FLAMES", command=play_flames)
play_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
