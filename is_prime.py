num = int(input("Enter the number : "))
is_prime = True
if num <= 1:
    is_prime = False
for x in range(2,num):
    if num%x == 0:
        is_prime = False
        break
if is_prime:
    print("Prime number")
else:
    print("NOt prime number")