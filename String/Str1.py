S = 'aaabbccccddeee'
count = 1
res = ''
for ind in range(0,len(S)):
    if ind+1 < len(S):
        if S[ind] == S[ind+1]:
            count += 1
        else:
            res += str(count)+S[ind]
            count = 1
    else:
        res += str(count) + S[ind]
print(res)