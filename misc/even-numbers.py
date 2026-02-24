start = int(input("Enter starting position: "))
stop = int(input("Enter stopping position: "))

print(f"Even numbers in range of {start} to {stop}:")
for i in range(start,stop+1):
    if i%2==0:
        print(i)



