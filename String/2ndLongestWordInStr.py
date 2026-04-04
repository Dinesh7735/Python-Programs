#2nd longest word in string
S = 'My name is dinesh'
L = S.split()
length=0
length2=0
for i in range(len(L)):
    if len(L[i])>length:
        pos = L.index(L[i])
        length = len(L[i])


for j in range(len(L)):
    if len(L[j])>length2:
        length2 = len(L[j])
        if length2<length:
            pos2 = L.index(L[j])


print(L[pos2])
print(len(L[pos2]))