#import demo
import getpass

username = "GabrielB"
password = "JohnGabriel123"

u = input("Input USERNAME ---> ")
p = getpass.getpass("Input PASSWORD ---> ")

if u == username and p == password :
	print("username correct and password correct")

else: 
	print("access denied")



