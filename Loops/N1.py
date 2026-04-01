s='a6b5c9'
L=[]
D=[]
for ch in s:
    if ch.isalpha():
        L.append(ch)
    else:
        D.append(int(ch))
k=0
for i in range(len(D)):
    for j in range(D[i]):
        print(L[k],end='')
    k+=1