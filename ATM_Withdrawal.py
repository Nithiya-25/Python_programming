balance = int(input("Enter your balance : "))
amount = int(input("Enter the amount to withdraw : "))
if amount <= balance:
    print("Withdraw successful")
else:
    print("Insufficient balance")