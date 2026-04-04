S = 'malayalam'
for ind in range(len(S)//2):
    if S[ind] != S[-ind-1]:
        print('Not Palindrome')
        break
else:
    print('Palindrome')