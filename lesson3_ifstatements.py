#Lesson 3 - Conditional statements 
#if statements

#Numerical If statements
age = int(input("enter your age: "))
if age >= 101:
    print("You're too old for this shit")
elif age < 0:
    print("You're joking right? you are not born yet!")
elif age >=18:
    print("you are now registered!")
else:
    print("You are no yet allowed to register!")
#string if statements
name = input("enter your name: ")
if name == "": #empty string
    print("Hey you son of a bitch, write your name!!")
else:
    print(f"Hello there {name}")
#using OR in if statements
response = input("Would you like some food? (Y/N): ")
if response == "Y" or response == "y": # use double equals  for difference, instead of assignement.
    print("Here have some enseladas")
else:
    print("Fine no food for you")
#using boolean in if statements
response = input("would you like an (x)AK-47 or (z)M16? (x or z)")
x= False
z=True
if x:
    print("Here is your AK-47, now spray em'")
else:
    print("Here's your M16, now export some freedom")