# Reverse a given number (e.g., 1234 → 4321) using a loop.

num = int(input("Enter a Number (eg: 3785) : "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number = ",reverse)