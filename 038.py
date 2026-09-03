# Print a right-angled triangle pattern of stars for n rows.

n = int(input("Enter a Number between 3 to 10 : "))

for i in range(1,n+1):
    print(i * "*", end="")
    print()
