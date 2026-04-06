num = 4
for row in range(num,0,-1):
    for sp in range(num-row):
        print(' ',end=' ')
    for col in range(1,row+1):
        if row == col or row == num or col == 1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()