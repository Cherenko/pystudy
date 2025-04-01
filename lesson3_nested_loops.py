# Nested loop = a loop within another loop (outer, inner)
#                outer loop:
#                       inner loop:
# Case 1 - using nested loops
#for x in range(3): # will execute the code 3 times. 
#    for y in range(1, 11):
#        print(y, end=" ") # use end with empty string to place numbers on the same line.
#    print()# Placing this will prin the number sequence per new line.


# CASE 2 - MAKING A SQUARE USING NESTED LOOPS
rows = int(input("enter the number of rows: ")) #setup number of Rows
columns = int(input("enter the number of columns: ")) #setup number of columns
symbol = input("enter a symbol to use: ") #setup symbol to use.

for x in range(rows): #will begin count based on rows
    for y in range(columns): #will beging count based on columns
        print(symbol, end="") #using symbol as placeholder
    print()
