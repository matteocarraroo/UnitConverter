# Title to user
print("This program converts units.")


# Function for metric
def convert_metric(unit_from, unit_to, value1):
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
    return calculation

def convert_temperature(unit_from, unit_to, value1):
    if unit_from == "celsius" and unit_to == "fahrenheit": calculation = ((value1 * 9 / 5) + 32)
    if unit_from == "celsius" and unit_to == "kelvin": calculation = (value1 + 273.15)
    if unit_from == "fahrenheit" and unit_to == "celsius": calculation = ((value1 - 32) * 5/9)
    if unit_from == "fahrenheit" and unit_to == "kelvin": calculation = ((value1 - 32) * 5/9 + 273.15)
    if unit_from == "kelvin" and unit_to == "celsius": calculation = (value1 - 273.15)
    if unit_from == "kelvin" and unit_to == "fahrenheit": calculation = ((value1 - 273.15) * 9/5 + 32)
    return calculation


available_units = ["nm", "mm", "cm", "m", "km", "celsius", "fahrenheit", "kelvin"]
unit_from = str(input(f"What unit would you like to convert from? (Please choose between {available_units}): "))
available_units.remove(unit_from)
unit_to = str(input(f"What unit would you like to convert to? (Please choose between {available_units}: "))
value1 = float(input(f"Choose a value in {unit_from} to convert from: "))

result = convert_temperature(unit_from, unit_to, value1)
print(f"The result is {result}{unit_to}")
