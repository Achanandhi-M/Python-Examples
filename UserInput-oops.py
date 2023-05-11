class Name:
    def __init__(self,name):#constructor
        self.name=name #self is similar to this

    def welcome(self):
        print('Welcome' , User.name)


userName=input('Enter your Name: ')
User= Name(userName)# object is User 


User.welcome();