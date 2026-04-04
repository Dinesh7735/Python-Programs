S = 'a2bB5C @P1 ^Hi'
res = ''
for ch in S:
    if not('0' <= ch <= '9' or 'A' <= ch <= 'Z' or 'a' <= ch <= 'z'):
        res += ch
print(res)