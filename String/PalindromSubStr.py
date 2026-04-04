S = 'abcba'
for si in range(0,len(S)):
    for ei in range(si+1,len(S)+1):
        word = S[si:ei]
        if word == word[::-1]:
            print(word)