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

        
        
    def calculateArea(self):  
        return self.length*self.width  


class Triangle(Shape):
    def __init__(self,object_type,base,height):
        super().__init__(object_type)
        self.base=base
        self.height=height
        
        
    def calculateTriangleArea(self):  
        return 0.5 * self.base * self.height 


def choice():
    print('Calculating Area of Rectangle and Triangle')
    userchoice=int(input('press 0 for Rectangle and 1 for Triangle:'))
    if userchoice==0:
        length=int(input('Enter the value of length: '))
        width=int(input('Enter the value of width :'))
        myobj=Rectangle('Rectangle',length,width)
        print('Object is :' , myobj.displayObject())
        print('Area of Rectangle:', myobj.calculateArea())

    elif userchoice==1:
        base=int(input('Enter the base value: '))
        height=int(input('Enter the height value :'))
        myobj1=Triangle('Triangle',base,height)
        print('Object is :' , myobj1.displayObject())
        print('Area of Triangle:', myobj1.calculateTriangleArea()) 

    else:
        print('Invalid choice')
        choice()       

choice()        