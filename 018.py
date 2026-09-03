# Find the largest of three numbers using if-elif-else.

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
num3 = int(input("Enter Third Number : "))

if num1 > (num2 and num3):
    print(f"{num1} is the Greatest")
elif num2 > (num1 and num3):
    print(f"{num2} is the Greatest")
else:
    print(f"{num3} is the Greatest")