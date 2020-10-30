class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.savings = BankAccount(0.05, 0)     # This is being autofed into the class BankAccount
        self.checking = BankAccount(0.10, 100)  # Do not add the argument names, just their values, the names already exist in the other class

    def make_withdrawl(self, amount, accountType):
        if accountType == "checking":
            if self.checking.balance < amount:
                print("Insuffecient Funds")
            else:
                self.checking.balance -= amount
        elif accountType == "savings":
            if self.savings.balance < amount:
                print("Insuffecient Funds")
            else:
                self.savings.balance -= amount
        return self

    def display_user_balance(self, accountType):
        if accountType == "checking":
            print(self.name, "Checking Balance:", self.checking.balance)
        elif accountType == "savings":
            print(self.name, "Savings Balance:", self.savings.balance)
        return self

    def make_deposit(self, amount, accountType):
        if accountType == "checking":
            self.checking.balance += amount
        elif accountType == "savings":
            self.savings.balance += amount
        return self

    def transfer(self, amount, accountType, receiver, recAccountType):
        if accountType =="checking":
            self.checking.withdrawl(amount)
        elif accountType =="savings":
            self.savings.withdrawl(amount)

        if recAccountType =="checking":
            receiver.checking.deposit(amount)
        elif recAccountType =="savings":
            receiver.savings.deposit(amount)
        return self
        
    def yield_interest(self, accountType):
        if accountType =="checking" and self.checking.balance > 0:
            interest = self.checking.int_rate * self.checking.balance
            self.checking.balance += interest
                
        elif accountType =="savings" and self.saings.balance > 0:
            interest = self.savings.int_rate * self.savings.balance
            self.savings.balance += interest
        return self

class BankAccount:
    def __init__(self, int_rate, balance):          # Values are added here from User class
        self.int_rate = int_rate
        self.balance = balance

    def withdrawl(self, amount):
        if self.balance < amount:
            print("Insuffecient Funds")
        else:
            self.balance -= amount
        return self  # Returning Self allows us to chain functions together by having the function call itself

    def display_account_info(self):
        print("Balance:", self.balance)
        return self

    def deposit(self, amount):
        self.balance += amount
        return self

    def yield_interest(self):
        if self.balance > 0:
            interest = self.int_rate * self.balance
            self.balance += interest
        return self

    def transfer(self, amount, receiver):
            self.withdrawl(amount)
            receiver.deposit(amount)


user1 = User("Adam", "adam@xyzmaling.com")
user1.make_deposit(1000000, "savings")
user1.make_withdrawl(1000000, "savings")
user1.make_deposit(1000000, "checking")
user1.transfer(100000, "checking", user1, "savings")
user1.make_withdrawl(100000000, "checking")
print(user1.checking.balance)
print(user1.savings.balance)
print(user1.name)
print(user1.email)
user1.make_withdrawl(100000000, "savings")
user1.yield_interest("checking")
print(user1.checking.balance)
print(user1.savings.balance)
user1.display_user_balance("checking")
user1.display_user_balance("savings")