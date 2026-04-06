num = 5
stars = 1
spaces = num//2
for row in range(1,num+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for col in range(1,stars+1):
        if col == 1 or col == stars:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    if row < num//2+1:
        stars += 2
        spaces -= 1
    else:
        stars -= 2
        spaces += 1