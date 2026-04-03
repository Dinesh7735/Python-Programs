M1 = [[1,2,3],[4,5,6],[7,8,9]]
M2 = [[1,4,4],[1,2,1],[0,3,6]]
res = []
if len(M1) == 0 and len(M2) == 0:
    print(res)
else:
    if len(M1[0]) == len(M2):
        for row in range(len(M1)):
            ele = []
            for col1 in range(len(M2[0])):
                Sum = 0
                for col2 in range(len(M2)):
                    Sum += M1[row][col2] * M2[col2][col1]
                ele.append(Sum)
            res.append(ele)
        print(res)
    else:
        print('Multiplication Not Possible')