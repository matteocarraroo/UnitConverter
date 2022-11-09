# Title to user
print("This program converts units.")
# Importing tkinter
import tkinter as tk


# Function for metric
def convert(unit_from, unit_to, value1):
    if unit_from == "mm" and unit_to == "cm": calculation = (value1 / 10)
    if unit_from == "mm" and unit_to == "m": calculation = (value1 / 1000)
    if unit_from == "mm" and unit_to == "km": calculation = (value1 / 1e+6)
    if unit_from == "mm" and unit_to == "nm": calculation = (value1 * 1e+6)
    if unit_from == "nm" and unit_to == "mm": calculation = (value1 / 1e+6)
    if unit_from == "nm" and unit_to == "cm": calculation = (value1 / 1e+7)
    if unit_from == "nm" and unit_to == "m": calculation = (value1 / 1e+9)
    if unit_from == "nm" and unit_to == "km": calculation = (value1 / 1e+12)
    if unit_from == "cm" and unit_to == "nm": calculation = (value1 * 1e+7)
    if unit_from == "cm" and unit_to == "mm": calculation = (value1 * 10)
    if unit_from == "cm" and unit_to == "m": calculation = (value1 / 100)
    if unit_from == "cm" and unit_to == "km": calculation = (value1 / 100000)
    if unit_from == "m" and unit_to == "nm": calculation = (value1 * 1e+9)
    if unit_from == "m" and unit_to == "mm": calculation = (value1 * 1000)
    if unit_from == "m" and unit_to == "cm": calculation = (value1 * 100)
    if unit_from == "m" and unit_to == "km": calculation = (value1 / 1000)
    if unit_from == "km" and unit_to == "nm": calculation = (value1 * 1e+12)
    if unit_from == "km" and unit_to == "mm": calculation = (value1 * 1e+6)
    if unit_from == "km" and unit_to == "cm": calculation = (value1 * 100000)
    if unit_from == "km" and unit_to == "m": calculation = (value1 * 1000)
    if unit_from == "celsius" and unit_to == "fahrenheit": calculation = ((value1 * 9 / 5) + 32)
    if unit_from == "celsius" and unit_to == "kelvin": calculation = (value1 + 273.15)
    if unit_from == "fahrenheit" and unit_to == "celsius": calculation = ((value1 - 32) * 5 / 9)
    if unit_from == "fahrenheit" and unit_to == "kelvin": calculation = ((value1 - 32) * 5 / 9 + 273.15)
    if unit_from == "kelvin" and unit_to == "celsius": calculation = (value1 - 273.15)
    if unit_from == "kelvin" and unit_to == "fahrenheit": calculation = ((value1 - 273.15) * 9 / 5 + 32)
    if unit_from == "cm3" and unit_to == "m3": calculation = (value1 / 1e+6)
    if unit_from == "cm3" and unit_to == "km3": calculation = (value1 / 1e+15)
    if unit_from == "m3" and unit_to == "cm3": calculation = (value1 * 1e+6)
    if unit_from == "m3" and unit_to == "km3": calculation = (value1 / 1e+9)
    if unit_from == "km3" and unit_to == "m3": calculation = (value1 * 1e+9)
    if unit_from == "km3" and unit_to == "cm3":
        calculation = (value1 * 1e+15)
    else:
        return None
    return calculation


# Initializing tkinter window components

# Creating window variable
root = tk.Tk()
# Scale value for integrating GUI program later
scale_value = tk.StringVar()
# Creating window with fixed not resizable size
root.title("Converter")
root.geometry("500x300")
root.resizable(True, True)

unit_from = tk.StringVar()
unit_from.set("Unit from")
unit_to = tk.StringVar()
unit_to.set("Unit to")

go_button = tk.Button(root)
input_output = tk.Entry(root)
input_output.insert("end", "Enter a value...")
value1 = input_output.get()
converted = tk.Label(root, text=convert(unit_from, unit_to, value1))
go_button.config(text="Convert!", command=lambda: [convert(unit_from, unit_to, value1), print()])

# Dictionaries to display correct name on drop-down
met_unit = {
    "Nanometers": "nm",
    "Millimeters": "mm",
    "Centimeters": "cm",
    "Meters": "m",
    "Kilometers": "km"
}

temp_unit = {
    "Celsius": "celsius",
    "Fahrenheit": "fahrenheit",
    "Kelvin": "kelvin",
}

vol_unit = {
    "Centimeters cubed": "cm3",
    "Meters cubed": "m3",
    "Kilometers cubed": "km3"
}

met_drop_to = tk.OptionMenu(root, unit_to, *met_unit)
temp_drop_to = tk.OptionMenu(root, unit_to, *temp_unit)
vol_drop_to = tk.OptionMenu(root, unit_to, *vol_unit)
met_drop_from = tk.OptionMenu(root, unit_from, *met_unit)
temp_drop_from = tk.OptionMenu(root, unit_from, *temp_unit)
vol_drop_from = tk.OptionMenu(root, unit_from, *vol_unit)


def gobutton():
    go_button.place(relx=0.5, rely=0.7)


def entrybox():
    input_output.place(relx=0.5, rely=0.5)


def vol_clicked_from():
    vol_drop_from.place(relx=0.10, rely=0.6)


def temp_clicked_from():
    temp_drop_from.place(relx=0.10, rely=0.6)


def met_clicked_from():
    met_drop_from.place(relx=0.10, rely=0.6)


def met_clicked_to():
    met_drop_to.place(relx=0.10, rely=0.4)


def temp_clicked_to():
    temp_drop_to.place(relx=0.10, rely=0.4)


def vol_clicked_to():
    vol_drop_to.place(relx=0.10, rely=0.4)


# Array to keep track of unit selected

available_units_metric = ["nm", "mm", "cm", "m", "km"]
available_units_temp = ["celsius", "fahrenheit", "kelvin"]
available_units_volume = ["cm3", "m3", "km3"]

# User chooses scale (temp, vol, metric
scale = scale_value

# Creating a label to prompt user to choose unit
tk.Label(root,
         text="""Choose a 
scale of units:""",
         justify=tk.CENTER).pack()

# Creating 3 radiobuttons
tk.Radiobutton(root,
               text="Temperature",
               variable=scale_value,
               # A lambda function is a small anonymous function
               command=lambda: [go_button.place_forget(), gobutton(), input_output.place_forget(), entrybox(),
                                vol_drop_to.place_forget(), met_drop_to.place_forget(), met_drop_from.place_forget(),
                                vol_drop_from.place_forget(), temp_clicked_to(), temp_clicked_from()],
               value="temperature").place(relx=0.1, rely=0.2)
tk.Radiobutton(root,
               text="Volume",
               variable=scale_value,
               command=lambda: [go_button.place_forget(), gobutton(), input_output.place_forget(), entrybox(),
                                met_drop_to.place_forget(), temp_drop_to.place_forget(), met_drop_from.place_forget(),
                                temp_drop_from.place_forget(), vol_clicked_from(), vol_clicked_to()],
               value="volume").place(relx=0.45, rely=0.2)
tk.Radiobutton(root,
               text="Metric",
               variable=scale_value,
               command=lambda: [go_button.place_forget(), gobutton(), input_output.place_forget(), entrybox(),
                                vol_drop_to.place_forget(), temp_drop_to.place_forget(), vol_drop_from.place_forget(),
                                temp_drop_from.place_forget(), met_clicked_to(), met_clicked_from()],
               value="metric").place(relx=0.75, rely=0.2)

converted.place(rely=1, relx=0.5)
# Window loop
root.mainloop()
while True:
     print(unit_from.get())
