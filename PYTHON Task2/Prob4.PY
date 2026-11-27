#encapsulation
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def display_balance(self):
        print("Balance:",self.__balance)
account=BankAccount(9000)
account.deposit(7000)
account.display_balance()

#encapsulation with attributes
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.__balance=balance
    def get_balance(self):
        print("Account Balance:",self.__balance)
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("Deposited:",amount)
        else:
            print("Invalid deposit amount")
    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
            print("Withdrawn:",amount)
        else:
            print("Insufficient balance or invalid amount")
account1=BankAccount("Ganesh",24000)
account1.get_balance()
account1.deposit(7000)
account1.withdraw(1800)
account1.get_balance()

#encapsulation with methods
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__update_balance(amount)
            print("Amount deposited successfully")
        else:
            print("Invalid deposit amount")
    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__update_balance(-amount)
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance or invalid amount")
    def display_balance(self):
        print("Account Holder:",self.name)
        print("Account Balance:",self.__balance)
    def __update_balance(self,amount):
        self.__balance+=amount
account1 = BankAccount("Ganesh",11000)
account1.display_balance()
account1.deposit(1000)
account1.withdraw(6000)
account1.display_balance()

#bank account details
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def display(self):
        print("Account Holder:",self.name)
        print("Balance:",self.__balance)
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("Amount Deposited:",amount)
        else:
            print("Invalid Amount")
    def __show_message(self):
        print("Account updated successfully")
    def update_account(self):
        self.__show_message()
account1=BankAccount("Hari",16000)
account1.display()
account1.deposit(3000)
account1.display()
account1.update_account()