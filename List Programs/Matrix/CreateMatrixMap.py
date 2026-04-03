rows = 3
column = 4
matrix = []
for row in range(rows):
    matrix.append(list(map(int,input(f'Enter {column} values: ').split())))
print(matrix)