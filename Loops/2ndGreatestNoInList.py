#Second greatest no in list
l=[4,6,1,5,9,34,12,78,98,66,134]
greatest=0
greatest2=0
for i in range(len(l)):
    if l[i]>greatest:
        greatest=l[i]
for j in range(len(l)):
    if l[j]>greatest2:
        if l[j]<greatest:
            greatest2=l[j]
print(f"2nd greatest number in the list is {greatest2}")