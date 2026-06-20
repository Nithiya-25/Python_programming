lst = list(map(int, input("Enter the elements : ").split()))
result = []
count = 0
for x in lst:
    if x == 0:
        count=count+1
        continue
    else:
        result.append(x)
for x in range(count):
    result.append(0)
print(result)
