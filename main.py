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

# Function for temperature
def convert_temperature(unit_from, unit_to, value1):
    if unit_from == "celsius" and unit_to == "fahrenheit": calculation = ((value1 * 9 / 5) + 32)
    if unit_from == "celsius" and unit_to == "kelvin": calculation = (value1 + 273.15)
    if unit_from == "fahrenheit" and unit_to == "celsius": calculation = ((value1 - 32) * 5 / 9)
    if unit_from == "fahrenheit" and unit_to == "kelvin": calculation = ((value1 - 32) * 5 / 9 + 273.15)
    if unit_from == "kelvin" and unit_to == "celsius": calculation = (value1 - 273.15)
    if unit_from == "kelvin" and unit_to == "fahrenheit": calculation = ((value1 - 273.15) * 9 / 5 + 32)
    return calculation

# Function for volume
def convert_volume(unit_from, unit_to, value1):
    if unit_from == "cm3" and unit_to == "m3": calculation = (value1 / 1e+6)
    if unit_from == "cm3" and unit_to == "km3": calculation = (value1 / 1e+15)
    if unit_from == "m3" and unit_to == "cm3": calculation = (value1 * 1e+6)
    if unit_from == "m3" and unit_to == "km3": calculation = (value1 / 1e+9)
    if unit_from == "km3" and unit_to == "m3": calculation = (value1 * 1e+9)
    if unit_from == "km3" and unit_to == "cm3": calculation = (value1 * 1e+15)
    return calculation

#Array to keep track of unit selected

available_units_metric = ["nm", "mm", "cm", "m", "km"]
available_units_temp = ["celsius", "fahrenheit", "kelvin"]
available_units_volume = ["cm3", "m3", "km3"]

#User chooses scale (temp, vol, metric
scale = str(input(f"Would you like to convert from/to temperature, metric or volume? "))

#If statements to check if units are in bounds
#Temperature if statement
if scale == "temperature":
    #Ask user unit to convert from
    unit_from = input(f"What unit would you like to convert from? (Please choose between {available_units_temp}): ")
    #Check value is in bounds
    if unit_from == str and unit_from in available_units_temp:
        #Remove unit chosen
        available_units_temp.remove(unit_from)
        #Ask user unit to convert to
        unit_to = input(f"What unit would you like to convert to? (Please choose between {available_units_temp}: ")
        #Check value is in bounds
        if unit_to == str and unit_to in available_units_temp:
            #Ask user value to convert
            value1 = input(f"Choose a value in {unit_from} to convert from: ")
            #Check value is in bounds
            if value1 == int or value1 == float:
                #Call calculation function
                result = convert_temperature(unit_from, unit_to, value1)
                #Output result
                print(f"The result is {result} degrees {unit_to}")
            else:
                print ("Choose a numeric value.")
        else:
            print("Please choose from the available units.")
    else:
        print("Please choose from the available units.")

#Metric if loop, procedure is the same as above
if scale == "metric":
    unit_from = input(f"What unit would you like to convert from? (Please choose between {available_units_metric}): ")
    if unit_from == str and unit_from in available_units_metric:
        available_units_metric.remove(unit_from)
        unit_to = input(f"What unit would you like to convert to? (Please choose between {available_units_metric}: ")
        if unit_to == str and unit_to in available_units_metric:
            value1 = input(f"Choose a value in {unit_from} to convert from: ")
            if value1 == int or value1 == float:
                result = convert_metric(unit_from, unit_to, value1)
                print(f"The result is {result}{unit_to}")
            else:
                print ("Choose a numeric value.")
        else:
            print("Please choose from the available units.")
    else:
        print("Please choose from the available units.")

#Volume if loop, procedure is the same as above
if scale == "volume":
    unit_from = input(f"What unit would you like to convert from? (Please choose between {available_units_volume}): ")
    if unit_from == str and unit_from in available_units_volume:
        available_units_volume.remove(unit_from)
        unit_to = input(f"What unit would you like to convert to? (Please choose between {available_units_volume}: ")
        if unit_to == str and unit_to in available_units_volume:
            value1 = input(f"Choose a value in {unit_from} to convert from: ")
            if value1 == int or value1 == float:
                result = convert_volume(unit_from, unit_to, value1)
                print(f"The result is {result}{unit_to}")
            else:
                print ("Choose a numeric value.")
        else:
            print("Please choose from the available units.")
    else:
        print("Please choose from the available units.")

#Prevent user from choosing out of bound values
else:
    print("Please choose between 'temperature', 'metric' or 'volume'.")



