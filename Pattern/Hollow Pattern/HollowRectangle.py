num = 4
for row in range(1,num+1):
    for col in range(num+1):
        if row == 1 or row == num or col == 0 or col == num:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()