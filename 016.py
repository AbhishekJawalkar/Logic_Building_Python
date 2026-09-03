# Check whether a number entered by the user is positive, negative, or zero.

Num = float(input("Enter a Number : "))

if Num > 0:
    print("Positive")
elif Num < 0 :
    print("Negative")
elif Num == 0:
    print("Zero")
else:
    print("Enter a Valid Number")

