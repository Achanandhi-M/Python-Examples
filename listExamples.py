myFirstList=[1,2,3,4,5]
mySecondList=[1,2,3,4,5]
result=[]
for i in range (len(myFirstList)):
    result.append(myFirstList[i] *  mySecondList[i])
print(result)
print(len(result))