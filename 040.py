# Keep asking the user to enter numbers until they enter -1, then print the sum of all entered numbers (use while with break).


sum = 0

while True:
    num = int(input("Enter a Number : "))

    if num == -1:
        break

    sum = sum + num

print("Sum =", sum)