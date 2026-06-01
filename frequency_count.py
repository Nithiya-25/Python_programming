lst = input("Enter the input to count : ").split() # handle string values for integer use  # lst = list(map(int , input("Enter the input to count : ")))
freq ={} # keeps the items
for i in lst:
    if i in freq:
        freq[i] = freq[i]+1 # if already present means increment the count
    else:
        freq[i] = 1
for i in freq:
    print(i, " : ",freq[i])