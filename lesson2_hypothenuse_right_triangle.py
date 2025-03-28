#calculate the hypothenuse of a right angle triangle.round
# formula c = sqrt(a^2 + b^2)
import math

a = float(input("What is side a?: "))
b = float(input("what is sdie b?: "))

c = math.sqrt(a**2 + b**2)

print(f"Hypotenuse is equal to: {round(c,2)}")
