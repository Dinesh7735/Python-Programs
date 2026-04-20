L = [13,232,2,11,22,343,54,11,23,43]
target = 11
ind = 0
while ind < len(L):
    if L[ind] == target:
        print(ind)
        break
    ind += 1
else:
    print(-1)