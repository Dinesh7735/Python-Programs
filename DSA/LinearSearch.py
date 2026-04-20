L = [1,32,4,56,8,99,3,4]
target = 4
for ind in range(len(L)):
    if L[ind] == target:
        print(ind)
        break
else:
    print(-1)