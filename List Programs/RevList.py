L = [10,5,7,40,20]

# print(L[::-1])

# L.reverse()
# print(L)

# res = []
# for ind in range(len(L)-1,-1,-1):
#     res.append(L[ind])
# print(res)

res = []
for ele in L:
    res = [ele] + res
print(res)
