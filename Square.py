class square:
    def __init__(self,value):
        self.value=value

    
    def calculateSquare(self):
        answer=self.value * self.value
        return answer





value=int(input('Enter the value : '))
myobj=square(value)
answer=myobj.calculateSquare()
print('Answer is ' , answer)