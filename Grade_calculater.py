try:
 mark = int(input("Enter mark : "))
 if mark >= 90:
    print("A Grade")
 elif mark >=80 and mark <=89:
    print("B Grade")
 elif mark >= 70 and mark <=79:
    print("C Grade")
 elif mark > 0 and mark < 70:
    print("D Grade")
 else:
    raise ValueError("Invalid mark")
except ValueError as e:
   print(e)
   