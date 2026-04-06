num = 13
for row in range(1,num+1):
    for col in range(1,num+1):
        if row <= num // 2+1:
            if row == col or col == 1:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        else:
            if row+col == num+1 or col == 1:
                print('*',end=' ')
            else:
                print(' ',end=' ')
    print()