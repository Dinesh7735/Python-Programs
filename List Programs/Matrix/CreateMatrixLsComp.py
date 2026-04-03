rows = 3
columns = 3
matrix = [list(map(int,input(f'Enter {columns} values: ').split())) for row in range(rows)]
print(matrix)