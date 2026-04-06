num = 5
spaces = 0
for ev in range(1,num+1):
    for space in range(spaces):
        print(' ',end=' ')
    for col in range(ev,num+1):
        print(col,end=' ') 
    print()
    spaces += 1