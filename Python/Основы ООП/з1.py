class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("На счете недостаточно средств")
        self.__balance -= amount

    def transfer(self, account, amount):
        if amount > self.__balance:
            raise ValueError("На счете недостаточно средств")
        self.withdraw(amount)
        account.deposit(amount)


account1 = BankAccount(100)
account2 = BankAccount(50)

print(account1.get_balance())
print(account2.get_balance())

account1.deposit(50)
account1.withdraw(30)
account1.transfer(account2, 20)

print(account1.get_balance())
print(account2.get_balance())