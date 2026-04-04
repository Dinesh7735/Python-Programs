S = 'a2b5c P1'
res = ''
for ch in S:
    if '0'<=ch<='9': #if ch.isdigit(): / if ch in '0123456789'
        res += ch
print(res)