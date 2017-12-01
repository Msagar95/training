class CustomerDetails:
    def __init__(self,balance):
        self.balance=balance

    def deposit(self,amt):
        self.balance+=amt
        print("Current Balance: ", self.balance)

    def withdraw(self,amt):
        self.balance-= amt
        print("Current Balance: ", self.balance)

    def balance(self):
        print("Current Balance: ", self.balance)

customer1=CustomerDetails(500)

while True:
    option=int(input("""
    1) Withdraw
    2) Deposit
    3) Show Balance
    """))
    if option == 1:
        x = int(input("Enter amount to be withdrawn: "))
        customer1.withdraw(x)
    elif option == 2:
        x = int(input("Enter amount to be deposited: "))
        customer1.deposit(x)
    elif option == 3:
        customer1.balance()
    else:
        print("Incorrect option")

    ch=input("Wanna continue? (y/n)")
    if ch == 'n':
        break

print("Thanks!")