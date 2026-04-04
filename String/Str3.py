S = '1aa2bc3c2d'
digit = ''
alpha = ''
res = ''
for ind in range(len(S)-1):
    if S[ind].isdigit():
        digit += S[ind]
    else:
        alpha += S[ind]
        if S[ind+1] >= len(S):
            break
        if S[ind+1].isdigit():
            res += int(digit)*alpha 
            digit = ''
            alpha = ''
res = int(digit)*alpha
print(res)