import tkinter as tk

# Create a function to handle button clicks
def button_click(event):
    current = result.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result.set(eval(current))
        except Exception as e:
            result.set("Error")
    elif text == "C":
        result.set("")
    else:
        result.set(current + text)

# Create a basic GUI window
window = tk.Tk()
window.title("Calculator")
# Create a text entry widget for displaying the result
result = tk.StringVar()
entry = tk.Entry(window, textvar=result, font=("Helvetica", 20))
entry.grid(row=0, column=0, columnspan=4)

# Define buttons and their positions
buttons = buttons = [
    ("7", 1, 0, 1), ("8", 1, 1, 1), ("9", 1, 2, 1), ("/", 1, 3, 1),
    ("4", 2, 0, 1), ("5", 2, 1, 1), ("6", 2, 2, 1), ("*", 2, 3, 1),
    ("1", 3, 0, 1), ("2", 3, 1, 1), ("3", 3, 2, 1), ("-", 3, 3, 1),
    ("0", 4, 0, 1), (".", 4, 1, 1), ("C", 4, 2, 1), ("+", 4, 3, 1),
    ("=", 5, 0, 2)
]

# Create and place buttons on the GUI
for (text, row, col, colspan) in buttons:
    button = tk.Button(window, text=text, padx=20, pady=20, font=("Helvetica", 16))
    button.grid(row=row, column=col, columnspan=colspan)
    button.bind("<Button-1>", button_click)

# Run the GUI main loop
window.mainloop()
