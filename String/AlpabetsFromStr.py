S = 'a2bB5c @p1 ^Hi'
res =''
for ch in S:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z': # if ch.isalpha()
        res += ch
print(res)