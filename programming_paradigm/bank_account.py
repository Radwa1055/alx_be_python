class BankAccount:
    def __init__(self, initial_balance=0):
        # نخزن الرصيد كـ float عشان التعامل مع الكسور يكون ثابت
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
        """
        ننسّق الرصيد:
       # - لو هو عدد صحيح (مثلاً 100.0) نظهره كـ "100"
        #- لو فيه كسور نظهره بمرّتين عشريتين "100.50"
        نطبع السطر EXACT: "Current Balance: 100" أو "Current Balance: 100.50"
        ونُعيد النص كقيمة return (مفيد للاختبارات الآلية).
        """
        bal = self.__account_balance
        if bal.is_integer():
            bal_str = str(int(bal))
        else:
            bal_str = f"{bal:.2f}"
        out = f"Current Balance: {bal_str}"
        print(out)
        return out



        