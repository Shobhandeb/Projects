import tkinter as tk

# Function to perform calculations
def calculate():
    try:
        result.set(eval(entry.get()))
    except:
        result.set("Error")

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Function to append numbers or operators to the entry field
def append_text(character):
    entry.insert(tk.END, character)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Variable to hold the result
result = tk.StringVar()

# Entry widget to display and input values
entry = tk.Entry(root, textvariable=result, font=("Arial", 14), bd=10, insertwidth=4, width=15, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons for numbers and operators
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create buttons in a grid
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 14), padx=10, pady=10, command=lambda t=text: append_text(t))
    button.grid(row=row, column=col)

# Clear and calculate buttons
clear_button = tk.Button(root, text="C", font=("Arial", 14), padx=10, pady=10, command=clear)
clear_button.grid(row=5, column=0, columnspan=3)

calculate_button = tk.Button(root, text="=", font=("Arial", 14), padx=10, pady=10, command=calculate)
calculate_button.grid(row=5, column=3)

# Run the main loop
root.mainloop()
