#Indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]

credit_number = "1234-5678-9012-3456"
credit_number1 = "1234-5678-9012-3456"
last_digits = credit_number[-4:]

#CASE 1
#print(credit_number[0]) #will print the character corresponding to the indexed "number"
#i.e, since the above indexed is '0' it will print character '1' from credit_number.

#CASE 2
#print(credit_number[0:4]) #This will print the characters starting '0' to '4'
#print(credit_number[:4]) # note: you can omit '0' as it will assume it starts at the beginning of the string.

#CASE 3
#print(credit_number[5:]) #This will print the characters starting '5' all the way to the end of the string.

#CASE 4
#print(credit_number[-3]) #will print the characters in reverse starting to the end of the string.

#CASE 5 - USING STEPS
#print(credit_number[::2]) #will print character every 2 character intervals.

#CASE 6 - Using last digits.
print(f"XXX-XXXX-XXXX-{last_digits}") #using the last digits, this will count the last 4 digits of the str.

#CASE 7 - Reversing a string.
credit_number1 = credit_number1[::-1] #will count the string in reverse step.
print(credit_number1)

