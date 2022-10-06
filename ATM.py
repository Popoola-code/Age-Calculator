#Program to deposit or withdraw from a machine
class Bank_account:
    def __init__(self):
        self.balance = 0
        print("Hey! Welcome to our deposit/ withdrawal machine")
    Password = int(input("\n Enter your password: "))
    
secret_number = 1990
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Try to Guess: '))
    guess_count +=1
    if guess == secret_number:
        print ('Welcome!')
        break
    else:
        print('Sorry, you failed!')
    
        print("Select option.")
        print("1 for Withdraw")
        print("2 for Transfer")
        print("3 for PayBills")
        while True:
    # take input from the user
            choice = input("Enter option(1/2/3): ")
            # check if choice is one of the four options
        if choice in ('1', '2', '3'):

    

            def deposit(self):
                amount = float(input("Enter amount to deposit: "))
                self.balance +=amount

        print("\n You have successfully deposited:", amount)

def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You have withdrawn:", amount)

        else:
            print("\n Sorry, your account balance is insufficient for the transaction")

def display(self):
        print("Here is your account balance:", self.balance)

d = Bank_account()
d.deposit()
d.withdraw()
d.display()        




# Python program to create Bankaccount class with both a deposit() and a withdraw() function
# class Bank_Account:
#     def __init__(self):
#         self.balance=0
#         print("Hi! Welcome to the Deposit/Withdrawal Machine.")
 
#     def deposit(self):
#         amount=float(input("Enter amount to be Deposited: "))
#         self.balance += amount
#         print("\n Amount Deposited:",amount)
 
#     def withdraw(self):
#         amount = float(input("Enter amount to be Withdrawn: "))
#         if self.balance>=amount:
#             self.balance-=amount
#             print("\n You Withdrew:", amount)
#         else:
#             print("\n Insufficient balance  ")
 
#     def display(self):
#         print("\n Net Available Balance=",self.balance)
 
# # Driver code
  
# # creating an object of class
# b = Bank_Account()
  
# # Calling functions with that class object
# b.deposit()
# b.withdraw()
# b.display()