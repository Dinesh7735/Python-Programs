S = 'aaaaabbbbccccdd'
res = {}
count = 1
for ind in range(len(S)-1):
    if S[ind] not in res:
        res[S[ind]] = 0
    if S[ind] == S[ind+1]:
        count += 1
    else:
        res[S[ind]] += count
        count = 1
res[S[ind]] += count
ml = max(res.values())
for key in res.keys():
    if res[key] == ml:
        print(key)
        break