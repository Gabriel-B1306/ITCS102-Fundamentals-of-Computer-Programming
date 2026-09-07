#breakdown fix money value to Ph Denominations
# 1000, 500, 200, 100,50, 20, 10, 5, 1

money= eval(input("Enter Money to Deposit ---->>>")) # int(), eval(), type()
#print(type(money))
print("============================ PH BANK DENOMATION ============================= ")
print(" MONEY TO DEPOSIT --------------->   ", money, "php")

libo  = money // 1000
libo_sukli = money % 1000

five_h =libo_sukli // 500
five_sukli = libo_sukli % 500

two_h =five_sukli // 200
two_sukli = five_sukli % 200

one_h = two_sukli // 100
one_h_sukli = two_sukli % 100

fifty = one_h_sukli // 50
fifty_sukli = one_h_sukli % 50

twenty = fifty_sukli // 20
twenty_sukli = fifty_sukli % 20

ten = twenty_sukli // 10
ten_sukli = twenty_sukli % 10

five = ten_sukli // 5
five_sukli2 = ten_sukli % 5
one = five_sukli2

print()
print("\n\t1000 - ", libo)
print("\t 500 - ", five_h)
print("\t 200 - ", two_h)
print("\t 100 - ", one_h)
print("\t 50  - ", fifty)
print("\t 20  - ", twenty)
print("\t 10  - ", ten)
print("\t 5   - ", five)
print("\t 1   - ", one)

