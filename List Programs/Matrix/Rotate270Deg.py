M = [[1,2,3],[4,5,6],[7,8,9]]
res = []
for ind1 in range(len(M)-1,-1,-1):
    row = []
    for ind2 in range(len(M[0])):
        row.append(M[ind2][ind1])
    res.append(row)
print(res)