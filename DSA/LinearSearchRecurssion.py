def Linear(L,target,ind = 0):
    if ind == len(L):
        return -1
    if L[ind] == target:
        return ind
    return Linear(L,target,ind+1)
L = [121,23,34,676,88,32,43,45,34]
target = 34
print(Linear(L,target))