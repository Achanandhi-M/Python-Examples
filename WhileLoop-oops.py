class MyWhile:
    def __init__(self,value):
        self.value=value


    def loop(self):
            n=0
            while n<=self.value:
                print('The value is ' , n)
                n+=1


value=int(input('Enter the value :'))
myobj=MyWhile(value)
myobj.loop()                