class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width


    def calculateRectangle(self):
        answer=self.length*self.width
        return answer #return statement is used to pass this value back to the caller of the method

length=int(input('Enter the length value :'))
width=int(input('Enter the width value : '))    
myobj=Rectangle(length,width)
result=myobj.calculateRectangle()
print('Area is ' , result)

