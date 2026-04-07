def square(num):
    return num**2
mapObj = map(square,range(1,6))
print(list(mapObj))