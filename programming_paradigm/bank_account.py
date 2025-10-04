# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional starting balance."""
        self.__account_balance = initial_balance  # خاصية خاصة (Encapsulation) عشان كا استخدم __ عشان محدش يقدر يير فيها من برة لكلاس 

    def deposit(self, amount):
        """Add amount to balance."""
        if amount > 0:
            self.__account_balance += amount  #نفس الحكاية 

    def withdraw(self, amount):
        """Withdraw amount if funds are sufficient."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):# استعلام عن الرصيد 
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance}")

    #لازم الفايلين يكونو في نفس الفولدر عشان اشغلهم مع بعض 
        
        