class BankAccount:
    def __init__(self, balance):
        self.__balance = balance


    def deposit(self, amount):
        self.__balance += amount


    def withdraw(self, amount):
        if self.__balance > amount:
            print("Недостаточно денег на балансе")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount(100)

print(account.get_balance())

account.deposit(100)

print(account.get_balance())

account.withdraw(200)

print(account.get_balance())

account.withdraw(200)