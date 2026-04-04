S = 'engineering'
res = ''
vowels = 'aeiouAEIOU'
ind = 0
while ind < len(S):
    if S[ind] in vowels:
        res += S[ind]
    ind += 1
print(res)