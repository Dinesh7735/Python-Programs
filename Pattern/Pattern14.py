num = 5
spaces = 0
for ev in range(num):
    for space in range(spaces):
        print(' ',end=' ')
    for col in range(num,ev,-1):
        print(col,end=' ')
    print()
    spaces += 1