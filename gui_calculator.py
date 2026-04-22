# gui_calculator.py

import tkinter as tk

# Function to update the input field
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(key))

# Function to clear the input
def clear():
    entry.delete(0, tk.END)

# Function to calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Input field
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Buttons layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        action = lambda x=btn: calculate() if x == '=' else press(x)
        tk.Button(frame, text=btn, font=("Arial", 14),
                  command=action).pack(side="left", expand=True, fill="both")

# Clear button
tk.Button(root, text="C", font=("Arial", 14), command=clear).pack(fill="both")

# Run app
root.mainloop()