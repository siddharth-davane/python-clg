BS= int(input("Enter Basic Salary of employee :"))

DA = BS*0.05
TA = BS*0.03
HRA= BS*0.12
GS = BS+DA+TA+HRA
tax= BS*0.1
net= GS-tax

print("DA :", DA)
print("TA :", TA)
print("HRA :", HRA)
print("Gross salary :", GS)
print("Tax :", tax)
print("Net salary :", net)
