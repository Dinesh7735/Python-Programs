S = 'a2bB5C @P1 ^Hi'
res = ''
for ch in S:
    if ch not in 'aeiouAEIOU' and ('A' <= ch <= 'Z' or 'a' <= ch <= 'z'):
        res += ch
print(res)