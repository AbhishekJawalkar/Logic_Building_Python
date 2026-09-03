# Take a student's marks and assign a grade (A/B/C/D/F) based on ranges.

Marks = int(input("Enter your marks (Out of 100) : "))

if Marks >= 80:
    print("Grade : A")
elif Marks >= 65:
    print("Grade : B")
elif Marks >= 50:
    print("Grade : C")
elif Marks >= 40:
    print("Grade : D")
elif Marks <= 30:
    print("Grade : F")
else:
    print("Enter Valid Marks")