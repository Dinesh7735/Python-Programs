S = 'engineering'
res = ''
for ch in S:
    if ch not in res:
        res += ch
print(res)