num = 7
spaces = num // 2
stars = 1
for row in range(num):
    for space in range(spaces):
        print(' ',end=' ')
    for col in range(stars):
        print('*',end=' ')
    print()
    if row < num//2:
        spaces,stars = spaces-1,stars+2
    else:
        spaces,stars = spaces+1,stars-2