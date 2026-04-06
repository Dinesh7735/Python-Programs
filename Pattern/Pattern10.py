num = 15
for row in range(num//2+1):
    for space in range(num//2-row):
        print(' ',end=' ')
    for col in range(row+1):
        print(chr(65+col),end=' ')
    for col in range(row,0,-1):
        print(chr(64+col),end=' ')
    print()
for row in range(num//2,0,-1):
    for space in range(num//2+1-(row)):
        print(' ',end=' ')
    for col in range(row):
        print(chr(65+col),end=' ')
    for col in range(row-1,0,-1):
        print(chr(64+col),end=' ')
    print()