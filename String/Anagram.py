S1 = 'listen'
S2 = 'silent'
if len(S1) == len(S2):
    for ch in S1:
        if ch not in S2 or S1.count(ch) != S2.count(ch):
            print('Not Anagram')
            break
    else:
        print('Anagram')
else:
    print('Not Anagram')