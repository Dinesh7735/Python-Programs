S = 'hello abcd hi efg'
word = ''
L = []
for ch in S:
    if ch == ' ':
        L = L + [word]
        word = ''
    else:
        word = ch + word
L = L + [word]
print(L)