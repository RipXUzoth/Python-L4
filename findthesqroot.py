import math
num = float(input("Enter a number: "))
if num < 0:
    print("Square root of a negative number is a complex number")
else:
    result = math.sqrt(num)
    print(f"The square rootof {num} is {result}")