# Given the radius of a circle, calculate its area and circumference.

radius = int(input("Enter the radius of the Circle : "))

area = 3.14 * radius**2
circum = 2 * 3.14 * radius

print(f"The Area of the Circle is : {area}")
print(f"The Circumference of the Circle is : {circum}")