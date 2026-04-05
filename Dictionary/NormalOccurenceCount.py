S = 'engineering'
res = {}
for ch in S:
    if ch not in res:
        res[ch] = 1
    else:
        res[ch] += 1
print(res)