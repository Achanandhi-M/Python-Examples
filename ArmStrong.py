userInput=int(input('Enter the value :'))
sum=0
length=len(str(userInput))
FinalValue=userInput
while userInput >0:
    modValue=userInput%10
    sum+=modValue ** length
    userInput//=10

if FinalValue == sum:
    print('Given Number is Armstrong')
else:
    print(' Given Number is Not Armstrong') 


