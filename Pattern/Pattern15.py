num = 5
spaces = num-1
for sv in range(num,0,-1):
    for space in range(spaces):
        print(' ',end=' ')
    for col in range(sv,num+1):
        print(col,end=' ')
    print()
    spaces -= 1