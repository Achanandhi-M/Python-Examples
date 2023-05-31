def is_even(num):
    return num % 2 == 0

userInput = int(input('Enter the value: '))

if is_even(userInput):
    print('The value:', userInput, 'is even')
else:
    print('The value:', userInput, 'is odd')
