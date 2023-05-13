class BankAccount:
    def __init__(self, AccNumber, Balance):
        self.AccNumber = AccNumber
        self.Balance = Balance

    def deposit(self, amount):
        if amount > 100:
            self.Balance += amount
            print('Amount is deposited')
            print('Balance is :', self.Balance)
        else:
            print('The Deposit amount should be greater than or equal to 100')    

    def withdraw(self, amount):
        if amount > self.Balance:
            self.Balance -= amount
            print('Amount is withdrawn')
            print('Balance:', self.Balance)
        else:
            print('Minimum Balance should be 1000.Cannot withdraw.')

    def balanceCheck(self):
        print('Balance:', self.Balance)



initialBalance = 1000  # minimum balance

def Input():
    AccNumber = int(input('Enter your Account number: '))
    userChoice = int(input('Enter 0 for Deposit, 1 for Withdraw, and 2 for Balance check: '))
    
    myobj = BankAccount(AccNumber, initialBalance)
    
    if userChoice == 0:
        depositAmount = int(input('Enter the amount to deposit: '))
        myobj.deposit(depositAmount)
    
    elif userChoice == 1:
        withdrawAmount = int(input('Enter the amount to withdraw: '))
        myobj.withdraw(withdrawAmount)
    
    elif userChoice == 2:
        myobj.balanceCheck()
    
    else:
        print('Invalid option. Re-enter the choice')
        Input()

Input()
