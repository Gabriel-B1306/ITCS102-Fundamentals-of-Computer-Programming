

name = input("What is your name ---->>> ")
item = input("What type of item is this ---->>> ")
isFragile = input("Is the item fragile (True/False) ---->>> ").lower() == 'true'
weight = eval(input("Weight in kg ---->>> "))
distance = eval(input("Distance in km ---->>> "))
is_express = input("Is this express shipping (True/False) ---->>> ").lower() == 'true'
is_international = input("Is this international shipping (True/False) ---->>> ").lower() == 'true'



base_cost = (weight * 2.50) + (distance * 0.15)

if weight <= 2.0 and distance <= 100 and is_express == False and is_international == False:
	total = 0.00
	level = "Free Shipping"
elif is_international == True and is_express == True:
	total = (base_cost * 1.40) + 50
	level = "International Express"
elif is_express == True or (is_international == True and weight > 20):
	total = (base_cost * 1.20) + 25
	level = "Express or Heavy International"
elif weight > 30 or distance > 1000:
	total = base_cost + 30
	level = "Oversized"
else:
	total = base_cost
	level = "Standard Rate"

print()
print("============================ GLOBAL FREIGHT SHIPPING CALCULATOR ============================= ")
print(" NAME --------------->   ", name)
print(" ITEM --------------->   ", item)
print(" FRAGILE ------------>   ", isFragile)
print(" WEIGHT -------------->   ", weight, "kg")
print(" DISTANCE ------------>   ", distance, "km")
print(" EXPRESS ------------->   ", is_express)
print(" INTERNATIONAL ------->   ", is_international)
print()
print("\tPRICING TIER  - ", level)
print("\tTOTAL COST    - php", total)
print("============================================================================================== ")