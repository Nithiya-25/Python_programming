#ATM Withdrawal
balance = int(input("Enter your balance : "))
amount = int(input("Enter the amount to withdraw : "))
if amount <= 0:
    print("Invalid amount")
elif amount <= balance:
    print("Withdraw successful")
    print("Remaining amount : ", balance-amount)
else:
    print("Insufficient balance")