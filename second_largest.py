lst = list(map(int ,input("Enter the list of numbers :  ").split()))
largest = second_largest = float('-inf')
smallest = second_smallest = float('inf')
for x in lst:
    if largest < x:
        second_largest = largest
        largest = x
    elif x != largest and second_largest < x:
        second_largest = x
    if smallest > x:
        second_smallest = smallest
        smallest = x
    elif x!=smallest and second_smallest > x:
        second_smallest = x
print("second largest number : ",second_largest)
print("second smallest number : ",second_smallest)