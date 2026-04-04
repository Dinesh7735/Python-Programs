S = 'hello'
res = ''
ind = -1
while ind >= -len(S):
    res += S[ind]
    ind -= 1
print(res)