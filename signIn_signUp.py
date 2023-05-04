def signIn(username2,password2):
    username1=input('Enter the Username: ')
    password1=input('Enter the password : ')
    if(username2 == username1 and password2 == password1 ):
        print('Thank you')
    else:
        print('Its seems your crenditals are wrong')
        creditsSetup=int(input('press 0 for signUp and 1 for logout: '))
        if(creditsSetup==0):
            signUp()
        elif(creditsSetup==1):
            print('See you soon :)')   
        else:
            print('Invalid choice please Enter correct option')               

def signUp():
    username2=input('Enter the Username: ')
    password2=input('Enter the password :')
    userChoice=input('Who is your favourite person :')
    interest=int(input("press 0 for signIn and 1 for exit: ?"))
    if(interest==0):
        signIn(username2,password2)
    elif(interest==1):
        print('Will see you soon:) ')  
    else:
        print('Invalid choice please Enter correct option') 
        signUp()     

# The program starts Here
print('Welcome')

#variable declaration
username1=''
password2=None
username2=None
password1=''
interest=0
creditsSetup=0

# First function Execution
def myOption():
    option = int(input('Press 0 for signIn and 1 for signUp: '))
    if option == 0:
        signIn(username2, password2)

    elif option == 1:
        signUp()

    else:
        print('Invalid choice please Enter correct option ')
        myOption()      

myOption()        