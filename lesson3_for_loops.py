# For Loops = execute a block of code a fixed number of times.
#              You can iterate over a range, string, sequence etc.
#range( start : end : step ) = range function for counting


for x in reversed(range(1, 11)): #will count 1 to 10. using "reversed()" function will count it backwards.
    print(x)

print("HAPPY NEW YEAR!")

for y in range(1,21):
    if y == 13:
        continue
    else:
        print(y)

