num = 5
for row in range(num,0,-1):
    for space in range(num-row):
        print(' ',end=' ')
    for col in range(row*2-1):
        print('*',end=' ')
    print()