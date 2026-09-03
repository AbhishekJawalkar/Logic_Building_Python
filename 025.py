# For a single number, print "Fizz" if divisible by 3, "Buzz" if divisible by 5, "FizzBuzz" if divisible by both, otherwise the number itself.

NUM = int(input("Enter a Number : "))

if NUM % 3 == 0 and NUM % 5 == 0 :
    print("FizzBuzz")
elif NUM % 3 == 0:
    print("Fizz")
elif NUM % 5 == 0:
    print("Buzz")
else:
    print(NUM)