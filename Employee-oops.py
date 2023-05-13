class Employee:
    def __init__(self,name,day,salary):
        self.name=name
        self.day=day
        self.salary=salary

    def calculateSalary(self):
        if(self.day > 28 and self.day <31):
            self.salary+=500
            print('Your Final salary:' , self.salary)

        elif (self.day <28):
            self.salary+=-500
            print('Your Final salary : ' , self.salary)

        else:
            print('Invalid number')  

        








name=input('Enter your Name: ')
day=int(input('Enter your no of days you are present: '))
salary=int(input('Enter your salary amount :'))
myobj=Employee(name,day,salary)
myobj.calculateSalary()