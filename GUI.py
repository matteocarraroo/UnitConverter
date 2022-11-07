# Importing tkinter
import tkinter as tk

# Creating window variable
root = tk.Tk()
# Scale value for integrating GUI program later
scale_value = tk.IntVar()
# Creating window with fixed not resizable size
root.title("Converter")
root.geometry("500x300")
root.resizable(False, False)

clicked_to = tk.StringVar()
clicked_to.set("Unit from")
clicked_from = tk.StringVar()
clicked_from.set("Unit to")

go_button= tk.Button(root)
input_output = tk.Entry(root)
input_output.insert("end", "Enter a value...")
go_button.config(text="Convert!", command= None)

met_unit = [
    "Nanometers",
    "Millimeters",
    "Centimeters",
    "Meters",
    "Kilometers"
]

temp_unit = [
    "Celsius",
    "Fahrenheit",
    "Kelvin",
]

vol_unit = [
    "Centimeters cubed",
    "Meters cubed",
    "Kilometers cubed"
]

met_drop_to = tk.OptionMenu(root, clicked_to, *met_unit)
temp_drop_to = tk.OptionMenu(root, clicked_to, *temp_unit)
vol_drop_to = tk.OptionMenu(root, clicked_to, *vol_unit)
met_drop_from = tk.OptionMenu(root, clicked_from, *met_unit)
temp_drop_from = tk.OptionMenu(root, clicked_from, *temp_unit)
vol_drop_from = tk.OptionMenu(root, clicked_from, *vol_unit)

def gobutton():
    go_button.place(relx=0.5, rely= 0.7)

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
               command=lambda: [go_button.place_forget(), gobutton(), input_output.place_forget(), entrybox(), vol_drop_to.place_forget(), met_drop_to.place_forget(), met_drop_from.place_forget(), vol_drop_from.place_forget(), temp_clicked_to(), temp_clicked_from()],
               value=1).place(relx=0.1, rely=0.2)
tk.Radiobutton(root,
               text="Volume",
               variable=scale_value,
               command=lambda: [go_button.place_forget(), gobutton(), input_output.place_forget(), entrybox(), met_drop_to.place_forget(), temp_drop_to.place_forget(), met_drop_from.place_forget(), temp_drop_from.place_forget(), vol_clicked_from(), vol_clicked_to()],
               value=2).place(relx=0.45, rely=0.2)
tk.Radiobutton(root,
               text="Metric",
               variable=scale_value,
               command=lambda: [go_button.place_forget(), gobutton(), input_output.place_forget(), entrybox(), vol_drop_to.place_forget(), temp_drop_to.place_forget(), vol_drop_from.place_forget(), temp_drop_from.place_forget(), met_clicked_to(), met_clicked_from()],
               value=3).place(relx=0.75, rely=0.2)
# Window loop
root.mainloop()
