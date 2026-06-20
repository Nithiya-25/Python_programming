#Password checker
password = input("Enter the password : ")
has_upper = False
has_lower = False
has_special = False
has_digit = False
if len(password) == 8:
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_special = True
    if has_upper and has_lower and has_special and has_digit:
        print("Valid Password")
    else:
        print("Invaild password")
else:
    print("Invalid password")
    