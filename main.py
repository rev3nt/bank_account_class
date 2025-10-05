class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance < amount:
            print("Недостаточно денег на балансе")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


options = '''\n1. Внести деньги на счет
2. Вывести деньги со счета
3. Вывести баланс счета
4. Выйти из программы\n'''

bank_account = BankAccount()

func_dict= {
    '1': lambda: bank_account.deposit(int(input('Введите количество денег для депозита: '))),
    '2': lambda: bank_account.withdraw(int(input('Введите сумму, которую хотите вывести: '))),
    '3': lambda: print(bank_account.get_balance())
}

while True:
    print(options)

    user_input = input('Введите номер опции: ').strip()

    if user_input == '4':
        break

    if user_input in func_dict:
        func_dict[user_input]()
    else:
        print('Введена некорректная опция!')