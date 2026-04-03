M1 = [[1,2,3],[4,5,6],[7,8,9]]
Sum = 0
if len(M1) == 0:
    print([])
else:
    if len(M1) == len(M1[0]):
        for row in range(len(M1)):
            for col in range(len(M1[0])):
                if row == col:
                    Sum += M1[row][col]
        print(Sum)
    else:
        print('Addition Not Possible')