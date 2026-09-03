# Check whether a number is an Armstrong number (e.g., 153 = 1³+5³+3³).

num = int(input("Enter a Number : "))

num1 = num
digits = len(str(num))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit**digits
    num = num // 10

if num1 == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")