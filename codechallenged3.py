print("=" * 160)
print("                                                                 GLOBAL GABBY SHIPPING CALCULATOR")
print("=" * 160)

name = input("What is your name? --> ")
item = input("What type of item is this? --> ")
isFragile = input("Is the item fragile (True/False) --> ")
weight = eval(input("Weight in kg --> "))
distance = eval(input("Distance in km --> "))
is_express = input("Is this express shipping (True/False) --> ")
is_international = input("Is this international shipping (True/False) --> ")

# convert the True/False text into an actual True/False value
isFragile = isFragile.lower() == "true"
is_express = is_express.lower() == "true"
is_international = is_international.lower() == "true"

base_cost = (weight * 2.50) + (distance * 0.15)

if weight <= 2.0 and distance <= 100 and is_express == False and is_international == False:
    total = 0.00
    tier = "Free Shipping"
elif is_international == True and is_express == True:
    total = (base_cost * 1.40) + 50
    tier = "International Express"
elif is_express == True or (is_international == True and weight > 20):
    total = (base_cost * 1.20) + 25
    tier = "Express or Heavy International"
elif weight > 30 or distance > 1000:
    total = base_cost + 30
    tier = "Oversized"
else:
    total = base_cost
    tier = "Standard Rate"

total = round(total, 2)

print("=" * 160)
print("Hi", name)
print("Your item is a", item)
print("Weight:", weight, "kg")
print("Distance:", distance, "km")
print("Fragile:", isFragile)
print("Pricing Tier:", tier)
print("Total Cost: ₱", total)
print("Thank you for using our shipping calculator!")
print("=" * 160)