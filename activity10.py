#basic if else program

username = "user1"
password = "Pogi123"

u = input("Input USERNAME ---> ")
p = input("Input PASSWORD ---> ")

if u == username and p == password :
	print("username correct and password correct")

else: 
	print("access denied")


if u == username and p == password:
    print("Login successful!")
else:
    print("Incorrect username or password.")
