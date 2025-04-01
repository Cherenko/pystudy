#format specifiers = {value:flags} format a value based on what
#                              the flags are inserted.


#.(number)f = round to what many decimal palce (fixed point)
# :(number) = allocate that many spaces.
# :03 = allocate and zero pad that many spaces.
# :< = left justify
# :> = right justify
# :^ = center justify
# :+ = use a plus sign to indicate positive value.
# := = place sign to leftmost position
# :  = insert a space before positive numbers.
# :, = comma separator.

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:.2f}") #adds to decimal point  aside floating point value.
print(f"Price 3 is ${price3:.1f}")# will onyly include/add 1 decimal point.
print(f"Price 2 is ${price2:10}") #will add 10 spaces
print(f"Price 3 is ${price3:010}") #will add 10 '0' padding.
print(f"Price 3 is ${price3:^10}") #will justify/place the value to center.
print(f"Price 3 is ${price3:+,.2f}") #You can combine with other compatible specifiers.
