S = 'abcba'
for si in range(0,len(S)):
    for ei in range(si+1,len(S)+1):
        word = ''
        for ind in range(si,ei):
            word += S[ind]
        print(word)