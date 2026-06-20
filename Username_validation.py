#Username_validation
name = input("Enter your UserName : ")
has_upper = False
has_lower = False
has_digit = False
has_underscore = False
has_space = False
if len(name)>=5 and len(name) <= 20:
    for x in name:
        if x.islower():
            has_lower = True
        elif x.isupper():
            has_upper = True
        elif x.isdigit():
            has_digit = True
        elif x == "_":
            has_underscore = True
        elif x==" ":
            has_space = True
    if has_upper and has_lower and has_digit and not has_space and has_underscore:
        print("Valid UserName")
    else:
        print("Invalid username")
else:
    print("Invalid Username")



