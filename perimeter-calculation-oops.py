class Shape:
    def __init__(self,object_type):
        self.object_type=object_type

    def displayObject(self):
        return self.object_type    


class Rectangle(Shape):
    def __init__(self,object_type,length,width):
        super().__init__(object_type)
        self.length=length
        self.width=width

        
        
    def calculatePerimeter(self):  
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self,object_type,a,b,c):
        super().__init__(object_type)
        self.a=a
        self.b=b
        self.c=c
        
        
    def calculateTrianglePerimeter(self):  
        return self.a + self.b + self.c


def choice():
    print('Calculating perimeter of Rectangle and Triangle')
    userchoice=int(input('press 0 for Rectangle and 1 for Triangle:'))
    if userchoice==0:
        length=int(input('Enter the value of length: '))
        width=int(input('Enter the value of width :'))
        myobj=Rectangle('Rectangle',length,width)
        print('Object is :' , myobj.displayObject())
        print('Perimeter of Rectangle:', myobj.calculatePerimeter())

    elif userchoice==1:
        a=int(input('Enter the value of a : '))
        b=int(input('Enter the value of b :'))
        c=int(input('Enter the value of c :'))

        myobj1=Triangle('Triangle',a,b,c)
        print('Object is :' , myobj1.displayObject())
        print('perimeter of Triangle:', myobj1.calculateTrianglePerimeter()) 

    else:
        print('Invalid choice')
        choice()       

choice()        