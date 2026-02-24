print("Enter marks of 3 subjects")

m1=int(input("Marks of subject 1: "))
m2=int(input("Marks of subject 2: "))
m3=int(input("Marks of subject 3: "))
m4=int(input("Marks of subject 4: "))
m5=int(input("Marks of subject 5: "))

total = m1+m2+m3+m4+m5
aggregate = total = total/5
printInfo = True

if m1 < 0 or m2 < 0 or m3 < 0 or m4 < 0 or m5 < 0 :
    print("Invalid Negative marks")
    printInfo = False

elif m1 > 100 or m2 > 100 or m3 > 100 or m4 > 100 or m1 > 100 :
    print("Invalid marks above 100")
    printInfo = False

elif m1 < 40 or m2 < 40 or m3 < 40 or m4 < 40 or m5 < 40 :
    print("Failed in one or more subjects")
    printInfo = False

elif aggregate < 50:
    print("Grade: 3rd Division")

elif aggregate < 60:
    print("Grade: 2nd Division")

elif aggregate < 75:
    print("Grade: 1st Division")

else:
    print("Grade: Distinction")

if(printInfo):
    print("Aggregate: ",aggregate)

