# Given three angles of a triangle, check if they form a valid triangle (sum to 180, each greater than 0).

print("Enter 3 Angles - Less than 180, More than 0")
angle1 = int(input("Enter First Angle : "))
angle2 = int(input("Enter Second Angle : "))
angle3 = int(input("Enter Third Angle : "))

if ((angle1 + angle2 + angle3) == 180 ):
    print("It is a Triangle")
else:
    print("Not a Valid Triangle")