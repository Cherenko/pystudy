# Excercise #2 - Shopping Cart Program

item = input("What items would you like to buy?: ")
price = float(input("what is the price?: "))
quantity = int(input("How many would you buy?: "))

total = price * quantity
print(f"The {item} costs a total of: P{total}")
