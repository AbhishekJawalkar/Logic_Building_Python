# Check whether a number is divisible by both 3 and 5 using logical operators, printing True/False.

num = int(input("Enter a Number : "))

if num%3 == 0 and num%5 == 0:
    print(True)
else:
    print(False)