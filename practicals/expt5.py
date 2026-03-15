length = int(input("Enter length of series:"))
f = 0
a=1
b=0

for i in range(length):
	print(f)
	f=a+b
	a=b
	b=f
