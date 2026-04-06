num = 5
for row in range(num,0,-1):
    for space in range(num-row):
        print(' ',end=' ')
    for col in range(0,row):
        print(chr(65+col),end=' ')
    for col in range(row-1,0,-1):
        print(chr(64+col),end=' ')
    print()