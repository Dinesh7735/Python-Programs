num = 5
spaces = num-1
for ev in range(num-1,-1,-1):
    for space in range(spaces):
        print(' ',end=' ')
    for col in range(num,ev,-1):
        print(col,end=' ')
    print()
    spaces -= 1