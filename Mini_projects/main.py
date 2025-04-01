#---------------- While Loop ---------------------

name = input("enter your name: ")

while name == "":
    print("You entered a blank name!: ")
    name = input("enter your name: ")
else:
    print(f"Hello {name}")

