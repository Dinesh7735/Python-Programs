def Even(num):
    return (num%10) % 2 == 0
print(list(filter(Even,[1234,250,420,0,123])))