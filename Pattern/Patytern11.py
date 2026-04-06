num = 9
spaces = num-1
for sv in range(1,num+1):
    for space in range(spaces):
        print(' ',end=' ')
    for col in range(sv,0,-1):
        print(col,end=' ')
    print()
    spaces -= 1