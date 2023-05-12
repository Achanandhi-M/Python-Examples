class Rectangle:

    @staticmethod
    def calculateRectangle(length,width):
        answer=length*width
        return answer



length=int(input('Enter the length value :'))
width=int(input('Enter the width value : '))    
result=Rectangle.calculateRectangle(length,width)
print('Area is ' , result)