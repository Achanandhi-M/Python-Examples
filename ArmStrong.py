
userInput=int(input('Enter the value :'))
sum=0
length=len(str(userInput))
FinalValue=userInput
while userInput >0:
    modValue=userInput%10 # Get the last digit of the number
    sum+=modValue ** length # Add the digit raised to the power of the number of digits to the sum
    userInput//=10 # Remove the last digit from the number

if FinalValue == sum:
    print('Given Number is Armstrong')
else:
    print(' Given Number is Not Armstrong') 


