# frequency count using set()
nums = list(map(int, input("Enter the list of inputs : ")))
unique = set(nums) # set is colletion of unordered unique elements
for x in unique:
    print(x, ":", nums.count(x)) # count is function used to count elements can use in list and tuple datatypes
#----------Summary--------
#time compleity - O(n^2) because count()
# Space complexity - O(k) k - unique elements