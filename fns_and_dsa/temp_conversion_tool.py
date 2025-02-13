FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32 )* FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

original_temp = input("Enter the temperature to convert: ")

if original_temp.isnumeric():

    temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if temp_type == "C":
        converted_temp = convert_to_fahrenheit(float(original_temp))
        print(f"{original_temp}°C is {converted_temp}°F")
    else:
        convert_to_celsius(original_temp)
        converted_temp = convert_to_celsius(float(original_temp))
        print(f"{original_temp}°F is {converted_temp}°C")
else:
    print("Invalid temperature. Please enter a numeric value.")