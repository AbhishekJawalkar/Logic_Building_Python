# Convert a temperature from Celsius to Fahrenheit, and another from Fahrenheit to Celsius.

Temp1 = int(input("Enter a Temperature (In Celsius) : "))
Temp2 = int(input("Enter a Temperature (In Fahrenheit) : "))

CeltoFah = (Temp1 * 9/5) + 32
FahtoCel = (Temp2 -32) * 5/9

print(f"Celsius to Fahrenheit = {CeltoFah:.2f}")
print(f"Fahrenheit to Celsius = {FahtoCel:.2f}")