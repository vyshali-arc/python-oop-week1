class BankAccount:
    def __init__(self, name, balance):
        self.name = name        # account holder name
        self.balance = balance  # initial balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)
        print("Updated Balance:", self.balance)
acc = BankAccount("Vyshali", 1000)
acc.deposit(500)
