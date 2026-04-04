S = 'a2bB5C @P1 ^Hi'
res = ''
for ch in S:
    if 'a' <= ch <= 'z': #res += ch.spapcase()
        res += chr(ord(ch)-32)
    elif 'A' <= ch <='Z':
        res += chr(ord(ch)+32)
    else:
        res += ch
print(res)