# Pythom weight converter

try:
    unit = input("Is this temperature in Celsius ir Fahrenheit (C/F): ")
except:
    print("That's not a number. Please enter a numeric value.")

temp = float(input("Enter the temperature: " ))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1) # round number to ,1 decimal place.
    print(f"The temperature in Fahrenheit is {temp}F ")
elif unit == "F":
    temp = round((temp - 32)* 5/9, 1)
    print(f"The temperature in Celsius is {temp}C ")  # round number to ,1 decimal place.
else:
    print(f"{unit} is an invalid unit of measurement")

