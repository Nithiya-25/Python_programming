quantity = int(input("Enter the number of items :"))
basic_bill = quantity*220
total_bill = basic_bill+basic_bill*18/100
if total_bill > 30000:
    print("Total bill amount : ",total_bill - (total_bill*30/100))
elif total_bill > 25000:
    print("Total bill amount : ",total_bill -(total_bill*20/100))
elif total_bill > 10000:
    print("Total bill amount : ",total_bill - (total_bill*15/100))
else:
    print("Total bill amount : ",total_bill)
