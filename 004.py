# Calculate the area and perimeter of a rectangle given its length and width entered by the user.

length = int(input("Enter the Length of the Rectangle : "))
width = int(input("Enter the Width of the Rectangle : "))

print(f"The Area of the Rectangle is : {length} x {width} = {length*width}")
print(f"The Perimeter of the Rectangle is : 2 x ({length} + {width}) = {2 * (length + width)}")