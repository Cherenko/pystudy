#While loop = execute some code WHILE some conditon remains true.

name = input("Enter your name: ")


#Using the IF to make input reiterations.
#if name == "":
#    print("you did not enter your name! you skimpy bastard")
#else:
#    print(f"Hello Herr {name}")

#Using WHILE to make input reiterations.
while name == "":
    print("you did not enter your name! you skimpy bastard")
    name = input("Enter your name: ")
print(f"Hello Herr {name}")
# This code will repeat keep repeating, untill there is an input from user.
# warning using this improperly might get you stuck in an infinite loop.

#Case 3
age = int(input("enter your Age: "))

while age <= 0:
    print("Kindly input your age you Sonofabitch!")
    age = int(input("Enter your Age: "))

print(f"Herr {name} you are {age} years old and qualified for combat!")

