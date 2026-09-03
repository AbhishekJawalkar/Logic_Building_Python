# Check whether a character entered by the user is a vowel or a consonant.

CHR = input("Enter a Letter : ").lower()

vowel = ["a","o","u","i","e"]

if CHR in vowel:
    print("It is a vowel")
else:
    print("It is a consonant")