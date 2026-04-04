S = 'engineering'
res = ''
ind = 0
while ind < len(S):
    if S[ind] not in res:
        res += S[ind]
    ind += 1
print(res)