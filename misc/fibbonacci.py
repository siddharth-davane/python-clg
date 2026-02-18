n=int(input("Enter number of fibbonachi numbers to generate:"))
f=0
a=0
b=1

for i in range(n):
    print(f)
    f=a+b
    b=a
    a=f

