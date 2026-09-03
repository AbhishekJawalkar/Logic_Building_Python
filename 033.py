# Check whether a number is a palindrome (e.g., 121, 1331).

num = int(input("Enter a Number : "))

num1 = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if num1 == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")