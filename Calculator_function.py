#Calculator using functions
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a = int(input("Enter the number1 : "))
b = int(input("Enter the number2 : "))
print("1.Addition 2.Subtraction 3.Multiplication 4.Division")
ch = int(input("Enter your choice : "))
if ch == 1:
    print("Result = ", add(a,b))
elif ch == 2:
    print("Result = ", sub(a,b))
elif ch == 3:
    print("Result = ", mul(a,b))
elif ch == 4:
    if b == 0:
        print("Invalid number2")
    else:
        print("Result = ", div(a,b))
else:
    print("Invalid choice")