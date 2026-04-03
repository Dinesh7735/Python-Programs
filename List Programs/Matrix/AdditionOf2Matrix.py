M1 = [[1,2,3],[4,5,6],[7,8,9]]
M2 = [[1,2,1],[1,4,4],[1,0,0]]
if len(M1) == 0 and len(M2) == 0:
    print([])
else:
    if len(M1) == len(M2) and len(M1[0]) == len(M2[0]):
        for row in range(len(M1)):
            for col in range(len(M1[0])):
                M1[row][col] = M1[row][col] + M2[row][col]
        print(M1)
    else:
        print('Addition Not Possible')