# frequency count
lst = input("Enter the input to count : ").split() # to handle string values for int and other datatypes use list(map())
freq ={}
for i in lst:
    freq[i] = freq.get(i,0)+1 # important function in datastructure familiar in frequency count its default value is set as 0
print(freq)
#---------Summary---------
#Time complexity - O(n)
# Space complexity - O(k) k-unique value count