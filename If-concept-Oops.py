class If:

    def __init__(self,value):
        self.value=value

    def condition(self):
            if value < 0 :
                print('The value you entered is Negative')
            elif value  > 0:
                print('The value you entered is positive')  
            else:
                print('The value you entered is zero')      



value=int(input('Enter the value :'))
myobj=If(value)
myobj.condition()