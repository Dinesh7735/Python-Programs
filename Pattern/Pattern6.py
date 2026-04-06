num = 5
for row in range(num):
    for col in range(row+1):
        print(chr(65+col),end=' ')
    print()
