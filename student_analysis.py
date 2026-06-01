
marks=int(input("Enter mark as list : "))
sum=0
num =0
count=0
min = marks[0]
max = marks[0]
for x in marks:
    sum = sum+ x
    count = count + 1
for x in marks:
    if min > x:
        min = x
for x in marks:
    if max < x:
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






