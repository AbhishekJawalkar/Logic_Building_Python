# Check whether a given year is a leap year.
"""
A year is a leap year if:
   -- It is divisible by 400, OR
   -- It is divisible by 4 but not divisible by 100

"""

Year = int(input("Enter a Year(XXXX) : "))

if Year%400 == 0:
    print("Leap Year")
elif (Year%4 == 0) and (Year%100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
