class ForLoop:

    def __init__(self,value):
        self.value=value

    def loop(self):
            if value < 0 :
                print('The value you entered is Negative')
            elif value  > 0:
                print('The value you entered is positive')  
            else:
                print('The value you entered is zero')      
3




value=int(input('Enter the value :'))
myobj=ForLoop(value)
myobj.loop()