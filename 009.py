# Convert a distance given in kilometers to miles, and one given in miles to kilometers.

KM = float(input("Enter the distance in KMs : "))
miles = KM * 0.621
print(f"Distance in Miles = {miles:.2f}")
ML = float(input("Enter the distance in Miles : "))
kms = ML * 1.609
print(f"Distance in Kilometers = {kms:.2f}")

