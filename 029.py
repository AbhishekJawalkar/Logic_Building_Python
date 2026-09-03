# Find the factorial of a number using a loop.

num = int(input("Enter a Number : "))

fact = 1
if num == (0 or 1):
    print("Factorial : 1")
else:
    for i in range(2,num+1):
        fact = fact * i
print(f"Factorial : {fact}")
