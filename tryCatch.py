value1=int(input('Enter the dividend value:'))
value2=int(input('Enter the divisor value:'))
answer=0
try:
   answer = value1 / value2
   print("The Quotient is " , answer)
except ValueError:
    print('Invalid Input')
except ZeroDivisionError:
    print('Cannot divide by Zero')
except OverflowError:
    print('value is overflowing')