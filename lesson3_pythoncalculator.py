#python calculator

operator = input("Enter an operator (+ - * /): ")

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    op_res = "Addition"
    print(f"{op_res} Result: {round(result, 3)}") #result is rounded to the nearest 3 digit value
elif operator == "-":
    result = num1 - num2 
    op_res = "Subtraction"
    print(f"{op_res} Result: {round(result, 3)}") 
elif operator == "*" :
    result = num1 * num2
    op_res = "Multiplication"
    print(f"{op_res} Result: {round(result, 3)}") 
elif operator == "/" :
    result = num1 / num2
    op_res = "Division"
    print(f"{op_res} Result: {round(result, 3)}") 
else:
    print(f"{operator} is not a valid value")