S = 'engineering'
res = ''
for ch in S:
    if ch in 'aeiouAEIOU':
        res += ch
print(res)