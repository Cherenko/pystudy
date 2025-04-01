#conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                         Print or assign one of two values based on a condition
#                         'X' if 'condition' else 'Y'

#C1
num = 8
#C2
a = 6
b = 7
#C3
age = 25
#C4
temperature = 30
#C5
user_role = "admin"

# Condition 1
#print("positive" if num > 0 else "Negative") # sample 'X' if 'condition' else 'Y'
#result = "EVEN" if num % 2 == 0 else "ODD" #'EVEN' IF NUMBER IS DIVISIBLE BY '2' IS IT EQUAL TO '0' ELSE 'ODD'
#print(result)

#Condition 2
#max_num = a if a > b else b # Return 'a' if a > b else return 'b'
#min_num = a if a < b else b # Return 'a' if a < b else retun 'b'

#Condition 3
#status = "Adult" if age >= 18 else "Child"
#print(status)

#Condition 4
#weather = "Hot" if temperature > 20 else "Cold"
#print(weather)

#Condition 5
access_level = "full Access" if user_role=="admin" else "Limited access"
print(access_level)