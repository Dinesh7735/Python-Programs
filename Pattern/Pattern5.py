num = 9
for row in range(1,num//2+1):
    for space in range((num//2+1)-row):
        print(' ',end=' ')
    for col in range(1,row+1):
        print(col,end=' ')
    for col in range(row-1,0,-1):
        print(col,end=' ')
    print()
for row in range(num//2+1,0,-1):
    for space in range((num//2+1)-row):
        print(' ',end=' ')
    for col in range(1,row+1):
        print(col,end=' ')
    for col in range(row-1,0,-1):
        print(col,end=' ')
    print()

    
