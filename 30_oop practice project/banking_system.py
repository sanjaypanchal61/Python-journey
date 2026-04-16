# ***********************BANKING SYSTEM PROJECT****************************

class Bank:
    bank_balance = 10000

    def debit(self,amount):
        self.bank_balance -= amount
        print(f"{amount} Debited Your Account")
        print(f"Total Balance: {self.bank_balance}")
    
    def credit(self,amount):
        self.bank_balance += amount
        print(f"{amount} Credited Your Account")
        print(f"Total Balance: {self.bank_balance}")


amt = float(input("Enter amount: "))
b = Bank()
b.debit(amt)