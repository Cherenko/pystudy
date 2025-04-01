#STRING METHODS - THINGS TO HELP WHEN WORKING WITH STRINGS.

#case1
name = input("Enter your full name: ")
result = len(name) #length function = will give the length of a string includes 'spaces', produces an integer.
result_1 = name.find(" ") #find method, will return of the first occurnece of a given character.
result_2 = name.find("B") #finds the first occurence of B in string 'name'
result_3 = name.rfind("s") #finds the last occurence of s in string. "reverse find"

print(result)
print(result_1)
print(result_2)
print(result_3)
#will return "-1" if character is not found.

#Case2 - string to UPPERCASE
name_1 = input("Enter Name to be capitalize: ")
name_1 = name_1.upper()
print(name_1)

#Case3 - string to LOWERCASE
name_2 = input("Enter Name to be capitalize: ")
name_2 = name_2.lower()
print(name_2)

#Case4 - isidigit method, will return either true or false if string contains only digits..
name_3 = input("Enter Name to be capitalize: ")
name_3 = name_3.isdigit()
print(name_3)

#case5 - isalpha method, will return true or false if string contains only alphabets.
name_4 = input("Enter Name to be capitalize: ")
name_4 = name_4.isalpha()
print(name_4)

#Other Methods
# result = phone_number.count("-") # counts the character given in the string.
# result = phone_number.replace("-", " ")# replaces the character "-" ion the string with " ".
# To remove a string just replace the " " with "" to act as an empty string.

#Note: use print(help(str)) - to print other string methods that you can use.


