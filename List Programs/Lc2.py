S = 'abcd'
print('\n'.join([S[ind] *(ind+1)for ind in range(len(S))]))