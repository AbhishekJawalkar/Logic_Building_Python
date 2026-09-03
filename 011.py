# Take a person's weight (kg) and height (m) and calculate their BMI using

weight = float(input("Enter your Weight(KG) : "))
height = float(input("Enter your Height(M) : "))

BMI = weight/height**2

print(f"Your BMI is : {BMI:.2f}")