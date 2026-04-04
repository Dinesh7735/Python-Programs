S = 'engineering'
res = ''
for ch in S:
    if ch not in res:
        print(f'{ch} - {S.count(ch)}')
        res += ch