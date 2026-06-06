# student analysis program 
marks=list(map(int,input("Enter the mark : ").split())) #datastructure used    map()- to notice & work || apply to each element
sum=0
num =0
count=0
min = marks[0]
max = marks[0]
for x in marks:
    sum = sum+ x # SUM PATTERN
    count = count + 1 # count pattern
    if min > x:   #running minimum pattern
        min = x
    if max < x:  #running maximum pattern
        max = x
avg = sum / count
for x in marks:
    if x > avg:
        num = num + 1
print("Total marks : ",sum)
print("Highest mark : ",max)
print("Lowest mark : ",min)
print("Average mark : ",avg)
print("Number of students who scored above avg mark is ", num)
# Time complexity  -  O(n)  for loop pattern
# Space complexity  -  O(1)  only new variables






