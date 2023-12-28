class BankAccount:

    def __init__(self, customer_name, account_number, balance, date_of_opening):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = date_of_opening

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("not enough money")
        else:
            self.balance -= amount

    def check_balance(self):
        print(f"Balance: {self.balance}")


x = BankAccount("Bruh", "231546432164", 45634654565465, "14/02/2020")
x.deposit(446465488)
x.check_balance()
x.withdraw(5465454654654)
x.check_balance()