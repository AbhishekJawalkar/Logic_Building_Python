# Print a number pyramid pattern for n rows.

n = int(input("Enter a Number between 3 to 10 : "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()
