num = 5
for row in range(1,num+1):
    for space in range(num-row):
        print(' ',end=' ')
    for col in range(2*row-1):
        print('*',end=' ')
    print()