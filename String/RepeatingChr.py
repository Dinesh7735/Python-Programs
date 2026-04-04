S = 'engineering'
res = ''
for ch in S:
    if ch not in res:
        if S.count(ch) > 1:
            print(ch)
        res += ch