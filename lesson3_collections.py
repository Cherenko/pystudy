# collections = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates ok
# set = {} unordered and imutable, but Add/Remove OK. No Duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER
import time

fruits = ["apple", "orange", "Banana", "Coconut", "pineapple"] # once bracket is placed the variable becomes a list.

print(fruits[0:2]) #you can use index operator with collections
# print(dir(fruits)) #---> to check directives of the collection
#print(help(fruits)) #---> get help for the directives
#print(len(fruits)) #---> length of the whole collection
print("apple" in fruits)



#for x in fruits:
#    print(x)
#    time.sleep(1)