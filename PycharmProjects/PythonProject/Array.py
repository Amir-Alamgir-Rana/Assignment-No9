# Q7: Encapsulation 

class BankAccount:
    # Constructor to initialize private attributes
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder      # public attribute
        self.__balance = balance                  # private attribute (Encapsulation)

    # Public method to access private balance
    def get_balance(self):
        return self.__balance

    # Public method to update private balance safely
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money safely
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance or invalid amount.")

# Create object of BankAccount
account = BankAccount("Ali", 1000)

# Accessing private variable using public methods (Encapsulation)
print("Current Balance:", account.get_balance())
account.deposit(500)
account.withdraw(300)
print("Updated Balance:", account.get_balance())

# Trying to access private variable directly (Not allowed)
# print(account.__balance)  # This will raise an AttributeError
