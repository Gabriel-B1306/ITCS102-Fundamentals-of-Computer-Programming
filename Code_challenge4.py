import getpass

username = "GabrielB"
password = "JohnGabriel123"

#login
Username = input("Enter username: ")
Password = input("Enter password: ")
#need login 
#username, password 
#loanee first name and job description

#prompt user to enter named/description of collateral e.g motorcycle, land, house,
#prompt user the value of the collateral, anything less than 30k is invalid

#maximum age for loan is 65
#ask user amount to loan, and the calculated interest rate using base rate
# if correct username and password, then prompt user to enter first name, job description, age, employment status, credit score, and annual income. Then calculate the interest rate based on the criteria provided.
if Username == username and Password == password:
    print("\nUsername correct and password correct. Welcome!")
    First_Name = input("Enter first name: ")
    Job_Description = input("Enter job description: ")
    age = int(input("Enter age: "))
    is_employed = input("Are you employed? (True/False): ")
    credit_score = int(input("Enter credit score: "))
    annual_income = float(input("Enter annual income: "))

    base_rate = 0.0
    # if age is between 21 and 65, and is employed, then check credit score and annual income to determine interest rate
    if age >= 21 and age <= 65 and is_employed == "True": #first criteria
        print("Passed baseline eligibility")
        if credit_score >= 750:
            if annual_income >= 100000:
                print("Your credit score is excellent and your income is high.")
                base_rate = 4.5
            else: # annual_income < 100000
                base_rate = 5.0
            print("Hi", First_Name + ", your interest rate is:", base_rate, "%")
            loan_amount = float(input("Enter loan amount requested: "))
            interest_amount = loan_amount * (base_rate / 100)
            print("Calculated Interest Amount:", interest_amount)
        # elif credit_score >= 600 and credit_score < 750: if not first criteria, then check if credit score is between 600 and 750, then check for collateral
        elif credit_score >= 600 and credit_score < 750: 
            collateral_desc = input("Enter description of collateral (e.g., motorcycle, land, house): ")
            collateral_value = float(input("Enter collateral value: "))
            has_collateral = collateral_value >= 30000
            #  if collateral value is less than 30,000, print a notice that the collateral value is invalid for rate reduction
            if not has_collateral:
                print("Notice: Collateral value under 30,000 is invalid for rate reduction.")
            if has_collateral:
                base_rate = 7.0
            elif annual_income < 40000:
                base_rate = 9.5
            else:
                base_rate = 8.0
            print("Hi", First_Name + ", your interest rate is:", base_rate, "%")
            loan_amount = float(input("Enter loan amount requested: "))
            interest_amount = loan_amount * (base_rate / 100)
            print("Calculated Interest Amount:", interest_amount)

        elif credit_score < 600:
            print("Credit score is too low")

    else:
        print("Rejected: Fails baseline criteria")

else:
    print("Access denied: Incorrect username or password")