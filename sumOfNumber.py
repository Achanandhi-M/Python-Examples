sum=0

n=int(input('Enter the value:'))

for i in range(0,n+1):
    sum=sum+i

if(sum<=1):
    print('Sum of',n, 'value is' , sum)
else:
     print('Sum of',n, 'values is' , sum)

