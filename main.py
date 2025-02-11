from bank_account import BankAccount
print("Welcome to you Bank Account")
#code without user inputs for pytest unit test check
balance = 100
account = BankAccount(balance)
print(f"Your Balance is :  {account.get_balance()}")
print("_____________________________________")
print(f"balance after deposit 50:  {account.deposit(50)}")
print("_____________________________________")
print(f"apply_Interest :  {account.apply_Interest()}")
print("_____________________________________")
print("_____________________________________")
print (f"balance after withdraw 30: {account.withdraw(30)}")
print("_____________________________________")
print(f"apply_Interest :  {account.apply_Interest()}")
print("_____________________________________")
print (f"transaction_history :  {account.transaction_history_print()}")
print("_____________________________________")
print (f"balance after commissions for {account.transaction_history_print()} transactions: {account.commissions_print()}")
print("_____________________________________")

#code with user inputs ..
#print("enter your balance please ! ")
#balance = input()
# balance = 100
# account = BankAccount(balance)
# print(f"Your Balance is :  {account.get_balance()}")
# print("_____________________________________")
# print("\nfor deposit press 1"
#       "\nfor withdraw press 2")
# choose = input()
# if choose ==  "1" :
#     print("Enter your deposit please!")
#     input_1 = int(input())
#     print("_____________________________________")
#     print(f"balance after deposit {input_1}:  {account.deposit(input_1)}")
#     print(f"apply_Interest :  {account.apply_Interest()}")
#     print("_____________________________________")
# elif choose ==  "2" :
#     print("Enter your withdraw please!")
#     input_1 = int(input())
#     print("_____________________________________")
#     print (f"balance after withdraw {input_1}: {account.withdraw(input_1)}")
#     print(f"apply_Interest :  {account.apply_Interest()}")
#     print("_____________________________________")
# else:
#     print (f"error input -> {choose}")
