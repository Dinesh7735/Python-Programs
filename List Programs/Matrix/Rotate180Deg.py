M = [[1,2,3],[4,5,6],[7,8,9]]
res = []
for ind1 in range(len(M)-1,-1,-1):
    row = []
    for ind2 in range(len(M[0])-1,-1,-1):
        row.append(M[ind1][ind2])
    res.append(row)
print(res)