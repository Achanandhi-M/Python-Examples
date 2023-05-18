class Fun:
    def __init__(self,mind):
        self.mind=mind

    def boring(self):
        print('Take rest :)')    

    def active(self):
        print('Enjoy your work') 

def userInput():
    mind=int(input('Enter 0 for boring mindset and 1 for active mindset : '))
    
    myobj=Fun(mind)
    if mind == 0:
        myobj.boring()
    elif mind == 1:
        myobj.active()    
    else:
        print('Your not in the universe')
        userInput()     

userInput()        