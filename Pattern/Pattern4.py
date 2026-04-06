num = 4
for row in range(num,0,-1):
    for space in range(num-row):
        print(' ',end=' ')
    for col in range(1,row+1):
        print(col,end=' ')
    for col in range(row-1,0,-1):
        print(col,end=' ')
    print()