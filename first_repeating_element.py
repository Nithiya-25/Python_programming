lst = list(map(int,input("Enter the list :").split()))
seen = set()
for i in lst:
    if i in seen:
        print(i)
        break
    seen.add(i)
        


