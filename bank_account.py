class BankAccount:
    def __init__(self,init_balance=0, interest_rate=0.06 ):
        #self.account_number = account_number
        self.balance = init_balance
        self.interest_rate = interest_rate
        self.transaction = []
        self.transaction_history=0
        self.commissions = 0
        #print (f"Account number: {self.account_number}")


    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            self.transaction.append(f"deposited {self.balance}")
            self.transaction_history +=1
            self.commissions +=1
        else:
            print("please enter correct amount for deposit")
        return self.balance


    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction.append(f"withdrawn {self.balance}")
            self.transaction_history += 1
            self.commissions += 1
        else:
            print("please enter correct amount for withdraw")
        return self.balance


    def get_balance(self):
        return self.balance


    def apply_Interest(self):
        monthly_price = self.interest_rate / 12
        monthly_interest = self.balance * monthly_price
        print("Apply_Interest information:") #repet
        print(f"monthly_price: {monthly_price} , monthly_interest: {monthly_interest}" )
        print(f"balance: {self.balance}")
        return self.balance+ monthly_interest


    def transaction_history_print(self):
        return self.transaction_history


    def commissions_print(self):
        transaction_commissions = 1.75
        print("Commissions information:")
        print(f"self.balance: {self.balance}")
        print(f"commissions per transaction price: {transaction_commissions}")
        print(f"self.transaction_history: {self.transaction_history}")
        ss = self.transaction_history * transaction_commissions
        return self.balance - ss


    def personal_loan(self,amount, return_time):
        #hlvaa
        pass


