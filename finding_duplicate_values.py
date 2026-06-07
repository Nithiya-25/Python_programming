# finding the duplicates value
lst = list(map(int,input("Enter the list :").split()))
seen = set()
duplicate = set()
for i in lst:
    if i in seen:
        duplicate.add(i)
    else:
        seen.add(i)
for i in duplicate:
    print(i,end = ",")
#Frequency / Seen Tracking Pattern
# Time complexity - O(n)
# Space complexity - O(n)
         
        


    