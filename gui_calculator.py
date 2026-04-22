# professional_calculator.py

import tkinter as tk

# Functions
def press(key):
    current = entry_var.get()
    entry_var.set(current + str(key))

def clear():
    entry_var.set("")

def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(str(result))
    except:
        entry_var.set("Error")

# Window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# Entry (Display)
entry_var = tk.StringVar()

entry = tk.Entry(
    root,
    textvariable=entry_var,
    font=("Segoe UI", 24),
    bd=0,
    bg="#1e1e1e",
    fg="white",
    justify="right"
)
entry.pack(fill="both", padx=10, pady=20, ipady=15)

# Buttons layout
buttons = [
    ['C', '(', ')', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=']
]

# Button styles
btn_bg = "#2d2d2d"
btn_fg = "white"
operator_bg = "#ff9500"

# Create buttons
for row in buttons:
    frame = tk.Frame(root, bg="#1e1e1e")
    frame.pack(expand=True, fill="both", padx=5, pady=5)

    for btn in row:
        if btn == "=":
            action = calculate
            bg_color = operator_bg
        elif btn == "C":
            action = clear
            bg_color = "#ff3b30"
        elif btn in "+-*/":
            action = lambda x=btn: press(x)
            bg_color = operator_bg
        else:
            action = lambda x=btn: press(x)
            bg_color = btn_bg

        tk.Button(
            frame,
            text=btn,
            font=("Segoe UI", 14, "bold"),
            bg=bg_color,
            fg=btn_fg,
            bd=0,
            command=action
        ).pack(side="left", expand=True, fill="both", padx=5, pady=5)

# Run app
root.mainloop()