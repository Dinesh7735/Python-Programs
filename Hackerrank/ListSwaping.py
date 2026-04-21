L = [2,0,4,1,0,8]
Zeros = []
for ele in L:
    if ele == 0:
        Zeros.append(ele)
        L.remove(ele)
L += Zeros
print(L)