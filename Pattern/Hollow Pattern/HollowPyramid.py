num = 5
for row in range(1,num+1):
    for sp in range(num - row):
        print(' ',end=' ')
    for col in range(1,2*row):
        if row == num or col == 1 or col == 2*row - 1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()