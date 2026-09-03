# Given three side lengths, determine whether the triangle is equilateral, isosceles, or scalene.

"""
Equilateral — all 3 sides equal
Isosceles — any 2 sides equal
Scalene — all 3 sides different

"""

print("Enter 3 Angles - Less than 180, More than 0")
angle1 = int(input("Enter First Angle : "))
angle2 = int(input("Enter Second Angle : "))
angle3 = int(input("Enter Third Angle : "))

if (angle1 == (angle2 and angle3) and ((angle1 + angle2 + angle3) == 180 )):
    print("Equilateral — all 3 sides equal")
elif ((angle1 == angle2) or (angle1 == angle3) or (angle3 == angle2)) and ((angle1 + angle2 + angle3) == 180 ):
    print("Isosceles — any 2 sides equal")
elif (angle1 != (angle2 and angle3) and ((angle1 + angle2 + angle3) == 180 )):
    print("Scalene — all 3 sides different")
else:
    print("Enter Valid Angles")
