# Print the multiplication table of a given number.

Num = int(input("Enter a Number : "))

for i in range(1,11):
    print(f"{Num} x {i} = {Num * i}")