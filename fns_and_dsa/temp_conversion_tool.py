FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
offset = 32

def convert_to_celsius(fahrenheit):
    return (fahrenheit - offset )* FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + offset

original_temp = int(input("Enter the temperature to convert: "))
temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if temp_type == "C":
    converted_temp = convert_to_fahrenheit(original_temp)
    print(f"{original_temp}°C is {converted_temp}°F")
else:
    convert_to_celsius(original_temp)
    converted_temp = convert_to_celsius(original_temp)
    print(f"{original_temp}°F is {converted_temp}°C")