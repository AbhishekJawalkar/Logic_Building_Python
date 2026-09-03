# Take the price of an item and a discount percentage, then calculate the final price after discount.

Price = float(input("Enter the price of the item : "))
Discount = float(input("Enter the Discount in % : "))

Amount = Price - (Price*Discount/100)

print(f"Final Amount = {Amount}")