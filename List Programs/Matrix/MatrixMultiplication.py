M1 = [[1,2,3],[4,5,6],[7,8,9]]
M2 = [[1,2,3],[4,5,6],[7,8,9]]
res = [[0,0,0],[0,0,0],[0,0,0]]
if len(M1) == 0 and len(M2) == 0:
    print([])
else:
    if len(M1) == len(M2) and len(M1[0]) == len(M2[0]):
        for row in range(len(M1)):
            for col in range(len(M1[0])):
                for col2 in range(len(M1[0])):
                    res[row][col] += M1[row][col2]*M2[col2][col]
        print(res)
               
    else:
        print('Multiplication Not Possible')