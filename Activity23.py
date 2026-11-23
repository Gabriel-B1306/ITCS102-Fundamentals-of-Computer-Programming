
#summation program 
name = input("Enter your name:---> ")
num= int(input("Enter a number:---> "))

def greet_me(name):
    print("Welcome to the program", (name))

def my_factorial(sagot):
    fact = 1
    for x in range(sagot,0,-1):
        fact *= x
    return fact
def my_summation(Lol):
    sum = 0
    for x in range(Lol,0,-1):
        sum += x
    return sum


print("output", my_factorial(4))
print("output", my_factorial(5))
print("output", my_factorial(6))
print("output", my_factorial(7))
print("---------------------------")
print("output", my_summation(4))
print("output", my_summation(5))
print("output", my_summation(6))
print("output", my_summation(7))

print("thank you  for using", greet(name))
