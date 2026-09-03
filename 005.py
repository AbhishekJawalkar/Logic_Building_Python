# Calculate compound interest given principal, rate, and time using the standard formula.

principal = int(input("Enter Principal Amount : "))
rate = float(input("Enter Rate of Interest : "))
time = int(input("Enter the Time(in years) : "))

ci = principal * (1 + rate/100)**time - principal
amount = principal * (1 + rate/100)**time 

print(f"The Compund Interest + Initial Amount is : {amount:.2f}")
print(f"The Compund Interest is : {ci:.2f}")