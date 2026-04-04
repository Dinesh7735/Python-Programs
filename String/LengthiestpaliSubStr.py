S = 'abcba'
L = []
for si in range(0,len(S)):
    for ei in range(si+1,len(S)+1):
        word = ''
        for ind in range(si,ei):
            word += S[ind]
        if word == word[::-1]:
            L.append(word)
maxlen = 0
lw = ''
for ele in L:
    if len(ele) > maxlen:
        maxlen = len(ele)
        lw = ele
print(f'Lengthiest word is \'{lw}\' \nLength of \'{lw}\' = {maxlen}')