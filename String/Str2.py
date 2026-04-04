S = '3a12b4c2d'
M = ''
res = ''
for ind in range(len(S)):
    if '0'<= S[ind] <= '9':
        M += S[ind]
    else:
        res += int(M) * S[ind]
        M =''
print(res)