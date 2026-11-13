amount = float(input("Enter the loan amount: ₱"))
yr = int(input("Input years to pay --->"))
months = yr * 12
principle = amount / months
rem_ballance = amount

for i in range(1, months + 1):
    rem_ballance -= principle
    interest = rem_ballance * 0.00256
    pay = principle + interest
    print (f"|   {i}\t| \t {round(pay, 2)}\t\t|\t {round(interest, 2)}\t|\t {round(principle, 2)}\t\t|\t {round(rem_ballance, 2)}\t\t|")
    
    
# ==========================================
# TASK #2: HOLLOW TRIANGLE PATTERN
# ==========================================
print("\n\n" + "="*50)
print("TASK #2: Hollow Triangle")
print("="*50 + "\n")

n = 7  # Number of rows (change this to make it bigger/smaller)

for i in range(1, n + 1):
    if i == 1:
        # Top: just 1 star
        print(" " * (n - i) + "*")
    elif i == n:
        # Bottom: full row of stars
        print("*" * (2 * n - 1))
    else:
        # Middle rows: hollow (star + spaces + star)
        inner_spaces = 2 * i - 3
        print(" " * (n - i) + "*" + " " * inner_spaces + "*")
        
        
# ==========================================
# TASK #3: Z PATTERN
# ==========================================
print("\n\nTASK #3")
print("Grade: 77 - 86\n")

n = 5  # size of the Z (5 rows and 5 columns)

for i in range(n):
    if i == 0 or i == n - 1:
        # Top and bottom rows: full line of stars
        print("*" * n)
    else:
        # Middle rows: spaces then one star
        # The star moves from right to left
        spaces = n - 1 - i
        print(" " * spaces + "*")