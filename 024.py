# Calculate an electricity bill where the rate per unit changes based on different consumption slabs.

Usage = float(input("Enter your monthly electricity usage (in Watts) : "))

if Usage >= 500:
    print(f"Your Bill is {Usage} x 5/Watt = {Usage*5}")
elif Usage >= 350:
    print(f"Your Bill is {Usage} x 6/Watt = {Usage*6}")
elif Usage >= 250:
    print(f"Your Bill is {Usage} x 7/Watt = {Usage*7}")
elif Usage >= 150:
    print(f"Your Bill is {Usage} x 8/Watt = {Usage*8}")
else:
    print(f"Your Bill is {Usage} x 9/Watt = {Usage*9}")
