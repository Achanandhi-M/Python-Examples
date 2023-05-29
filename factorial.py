def factorial(n):
    if n==0:
        return 1

    else:
        return n * factorial(n-1)


n=int(input('Enter the value :'))       

answer=factorial(n)

print('The Factorial of ' , n ,'is', answer)