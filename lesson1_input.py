# Excercise 1 - Recctangle Area Calculator
# Formula: A = l*w

print("Input the necessary values to find the Area of a rectangle")
l = float(input("What is the length?: ")) #using float for decimals
w = float(input("what is the width?: ")) #you can use int, if it's only absolute values.

A = l*w 
print(f"the area of the rectangle is: {A}cm²")
