# Excercise - Get the Circumference, Area and diameter of a Circle.
import math

r = float(input("What is the radius the Circle?: "))
C = 2*math.pi*r
A = math.pi*r**2
d = 2*r

#Formula of circumference of a Circle C= 2*pi*r
# you can use math.floor() to round down a number.
print(f"The circumference of the Circle is:{round(C, 2)}")

#Area of a Circle A=math.pi*r**2
# you can use the ff notation: A = math.pi*pow(r,2)
print(f"The Area of the Circle is: {round(A, 2)}cm^2")

#Diameter of a Circle d = 2*r
print(f"The Diameter of a Circle is: {round(d, 2)}")
