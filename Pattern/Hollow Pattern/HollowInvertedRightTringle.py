num = 5
for row in range(num,0,-1):
    for col in range(1,row+1):
        if row == num or row == col or col == 1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()