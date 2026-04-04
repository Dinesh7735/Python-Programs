S = 'hello abcd hi efg'
word = ''
L = []
for ch in S:
    if ch == ' ':
        L = [word] + L
        word = ''
    else:
        word += ch
L = [word] + L
print(L)