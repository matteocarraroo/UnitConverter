# Title to user
print("This program converts units.")


# Function for metric
def convert_metric(unitfrom, unitto, value1):
    if unitfrom == "mm" and unitto == "cm":
        calculation = value1 / 10
        return calculation
    elif unitfrom == "mm" and unitto == "m":
        calculation = value1 / 1000
        return calculation
    elif unitfrom == "mm" and unitto == "km":
        calculation = value1 / 1e+6
        return calculation
    elif unitfrom == "mm" and unitto == "nm":
        calculation = value1 * 1e+6
        return calculation
    elif unitfrom == "nm" and unitto == "mm":
        calculation = value1 / 1e+6
        return calculation
available_units = ["nm", "mm", "cm", "m", "km"]
unitfrom = str(input(f"What unit would you like to convert from? (Please choose between {available_units}): "))
available_units.remove(unitfrom)
unitto = str(input(f"What unit would you like to convert to? (Please choose between {available_units}: "))
value1 = float(input(f"Choose a value in {unitfrom} to convert from: "))

result = convert_metric(unitfrom, unitto, value1)
print(f"The result is {result}")
