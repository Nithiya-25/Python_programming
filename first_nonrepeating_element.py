lst = list(map(int, input("Enter the list").split()))
freq = {}
for x in lst:
    freq[x] = freq.get(x,0)+1
for i in lst:
    if freq[i]==1:
        print(i)
        break
