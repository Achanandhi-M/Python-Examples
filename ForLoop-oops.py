class Forloop:

    def __init__(self,value):
        self.value=value

    def loop(self):
        for i in range (self.value):
              print('The value is', i)



value=int(input('Enter the value: '))
myobj=Forloop(value)
myobj.loop()              