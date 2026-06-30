import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        temp = float(entry_temp.get())
        choice = conversion_var.get()

        if choice == "Celsius to Fahrenheit":
            result = (temp * 9/5) + 32
            output.config(text=f"{result:.2f} °F")

        elif choice == "Celsius to Kelvin":
            result = temp + 273.15
            output.config(text=f"{result:.2f} K")

        elif choice == "Fahrenheit to Celsius":
            result = (temp - 32) * 5/9
            output.config(text=f"{result:.2f} °C")

        elif choice == "Fahrenheit to Kelvin":
            result = (temp - 32) * 5/9 + 273.15
            output.config(text=f"{result:.2f} K")

        elif choice == "Kelvin to Celsius":
            result = temp - 273.15
            output.config(text=f"{result:.2f} °C")

        elif choice == "Kelvin to Fahrenheit":
            result = (temp - 273.15) * 9/5 + 32
            output.config(text=f"{result:.2f} °F")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# Main Window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")

# Heading
tk.Label(root, text="Temperature Converter",
         font=("Arial", 16, "bold")).pack(pady=10)

# Temperature Input
tk.Label(root, text="Enter Temperature:").pack()
entry_temp = tk.Entry(root, width=20)
entry_temp.pack(pady=5)

# Conversion Options
conversion_var = tk.StringVar()
conversion_var.set("Celsius to Fahrenheit")

options = [
    "Celsius to Fahrenheit",
    "Celsius to Kelvin",
    "Fahrenheit to Celsius",
    "Fahrenheit to Kelvin",
    "Kelvin to Celsius",
    "Kelvin to Fahrenheit"
]

tk.OptionMenu(root, conversion_var, *options).pack(pady=10)

# Convert Button
tk.Button(root, text="Convert",
          command=convert,
          bg="lightblue").pack(pady=10)

# Result Label
output = tk.Label(root, text="Result will appear here",
                  font=("Arial", 12))
output.pack(pady=10)

root.mainloop()