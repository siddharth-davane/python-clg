elements=int(input("Enter number of elements:"))
numList=[]

for i in range(elements):
    num=int(input("Enter element: "))
    numList.append(num)


print("Maximum:",max(numList))
print("Minimum:",min(numList))
print("Sum:",sum(numList))
print("Average:",sum(numList)/elements)
