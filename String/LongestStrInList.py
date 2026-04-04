#Finding longest string in the list
L=['Dinesh','Jack','Roshan','Jaganath']
length=0
for i in range(len(L)):
    if len(L[i])>length:
        pos = L.index(L[i])
        length = len(L[i])
print(L[pos])
print(length)

