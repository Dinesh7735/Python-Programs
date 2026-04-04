S = 'a2bB5C @P1 ^Hi'
res = ''
for ch in S:
    if 'a' <= ch <= 'z': #if ch.islower():
        res += chr(ord(ch)-32)
    else:
        res += ch
print(res)