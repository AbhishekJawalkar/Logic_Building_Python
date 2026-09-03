# Find the sum of all natural numbers from 1 to N using a loop.

Num = int(input("Enter a Number : "))

print(f"Printing the Sum of all natural numbers starting from 1 to {Num}")

sum = 0

for i in range(1, Num + 1):
    sum = sum + i

print(f"The Sum is : {sum}")