# Take marks of 5 subjects as input and print the total and average.

marks = list(map(int, input("Enter Marks of 5 Subjects : ").split()))

total = 0

for i in marks:
    total = total + i

average = total/len(marks)

print(f"The Total Marks is : {total}")
print(f"The Average is : {average}")

