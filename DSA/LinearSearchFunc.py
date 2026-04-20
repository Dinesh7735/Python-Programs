def Linear(L,targe):
    for ind in range(len(L)):
        if L[ind] == target:
            return ind
            break
    return -1
L = [121,232,43,55,67,43,67,323]
target = 67
print(Linear(L,target))