class BankAccount:
    def __init__(self, initial_balance=0):
        # الرصيد الابتدائي (float للتعامل مع الكسور)
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        amt = float(amount)
        if amt > 0:
            self.__account_balance += amt

    def withdraw(self, amount):
        amt = float(amount)
        if 0 < amt <= self.__account_balance:
            self.__account_balance -= amt
            return True
        else:
            return False

    def display_balance(self):
        # الطباعة مطابقة لتنسيق ALX: $xxx.xx
        print(f"Current Balance: ${self.__account_balance:.2f}")

    
        



        