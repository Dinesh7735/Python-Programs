L = [10,20,30,40,50]
for ind in range(len(L)//2):
    L[ind], L[-ind-1] = L[-ind-1], L[ind]
print(L)