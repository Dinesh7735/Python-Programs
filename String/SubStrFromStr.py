S ='abcde'
for si in range(0,len(S)):
    for ei in range(si+1,len(S)+1):
        print(S[si:ei])