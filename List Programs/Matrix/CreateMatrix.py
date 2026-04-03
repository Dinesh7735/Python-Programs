rows = 3
columns = 3
matrix = []
val = 1
for row in range(rows):
    L = []
    for col in range(columns):
        L.append(val)
        val += 1
    matrix.append(L)
print(matrix)