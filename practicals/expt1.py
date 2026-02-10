BS = int(input("Enter Employee's salary: "))

HRA = BS * 0.1
TA = BS * 0.05

total = BS + HRA + TA
proTax = total * 0.02
net = total - proTax


print("Basic salarry:",BS)
print("HRA:",HRA)
print("TA:",TA)
print("Total salary:",total)
print("Professional Tax:",proTax)
print("Net salary:",net)
