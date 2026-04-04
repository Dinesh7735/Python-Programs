S = 'abcba'
for si in range(0,len(S)):
    for ei in range(si+1,len(S)+1):
        for ind in range(si,ei):
            print(S[ind],end='')
        print()