#need login 
#username, password 
#loanee first name and job description

#prompt user to enter named/description of collateral e.g motorcycle, land, house,
#prompt user the value of the collateral, anything less than 30k is invalid

#maximum age for loan is 65
#ask user amount to loan, and the calculated interest rate using base rate
import getpass

username = "GabrielB"
password = "JohnGabriel123"

Username = input("Enter username: ")
Password = input("Enter password: ")
First_Name = input("Enter first name: ")
Job_Description = input("Enter job description: ")
age = int(input("Enter age: "))
is_employed = bool(input("Are you employed? (True/False): "))
credit_score = int(input("Enter credit score: "))
annual_income = float(input("Enter annual income: "))
has_collateral = bool(input("Do you have collateral? (True/False): "))

if Username == username and Password == password :
	print("username correct and password correct")

else: 
	print("access denied")
base_rate = 0.0
if age >= 21 and is_employed == True:
    print("Passed baseline eligibility")
    if credit_score >= 750:
        if annual_income >= 100000:
            print("Your credit score is excellent and your income is high. You qualify for the best interest rate.")
            base_rate = 4.5
        else:
            base_rate = 5.0
        print("Hi your interest rate is:", base_rate)

    elif credit_score >= 600 and credit_score < 750:
        if has_collateral == True:
            base_rate = 7.0
        elif annual_income < 40000:
            base_rate = 9.5
        else:
            base_rate = 8.0
        print("Approved! Final Interest Rate:", base_rate)

    elif credit_score < 600:
        print("Credit score is too low")
else:
    print("Rejected: Fails baseline criteria")  