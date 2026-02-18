rollnumber = int(input("Enter Roll number: "))
name = input("Enter Name: ")
division =  input("Enter Division: ")
m1=  int(input("Enter marks of sub 1: "))
m2=  int(input("Enter marks of sub 2: "))
m3=  int(input("Enter marks of sub 3: "))
m4=  int(input("Enter marks of sub 4: "))
m5=  int(input("Enter marks of sub 5: "))

total= m1+m2+m3+m4+m5
aggregrate = total/5

print("\n")
print("Roll number: ",rollnumber)
print("Name: ",name)
print("Division: ",division)
print("Total marks: ",total)
print("Aggragrate: ", aggregrate)
print("Entered marks: ",m1,m2,m3,m4,m5)
