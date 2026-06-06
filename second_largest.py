# program for finding second largest and smallest number
lst = list(map(int ,input("Enter the list of numbers :  ").split())) # list() used to handle data as list datastructure
largest = second_largest = float('-inf') # real number assume value 
smallest = second_smallest = float('inf')
for x in lst:
    if largest < x:  # Running maximum pattern 
        second_largest = largest #Used to maintain the previous value for the second largest value
        largest = x
    elif x != largest and second_largest < x:
        second_largest = x
    if smallest > x:   # Running minimum pattern 
        second_smallest = smallest
        smallest = x
    elif x!=smallest and second_smallest > x:
        second_smallest = x
print("second largest number : ",second_largest)
print("second smallest number : ",second_smallest)
# Time complexity - O(n) for loop pattern
# space complextity - O(1) new variable only used