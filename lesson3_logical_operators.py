# logical operators = evaluate multiple conditions (or, and, not)
#               or = at least one condition must be True
#               and = both conditions must be True
#               not = inverts the condition (not False, not True)  


#1 Using "or"
temp_c = 36
is_raining = False

if temp_c > 35 or temp_c < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event event is still scheduled")

#2 Using "and"
temp_a = 20
is_sunny = True

if temp_a >= 28 and is_sunny: # If temp_a is greater or equal to 28 and is sunny (True)
    print("It is HOT Outside!")
    print("It is SUNNY")
elif temp_a <= 0 and is_sunny: # If temp_a is less than or equal to 0 and is sunny (True)
    print("It is COLD outside ")
    print("It is SUNNY")
elif 28 > temp_a > 0 and is_sunny:
    print("It is WARM outside ")
    print("It is SUNNY")
#3 Using "not"
if temp_a >= 28 and not is_sunny:
    print("It is HOT Outside!")
    print("It is CLOUDY")
elif temp_a <= 0 and not is_sunny:
    print("It is COLD outside ")
    print("It is CLOUDY")
elif 28 > temp_a > 0 and not is_sunny:
    print("It is WARM outside ")
    print("It is CLOUDY")