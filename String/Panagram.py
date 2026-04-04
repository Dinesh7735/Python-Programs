S = 'the quick brown fox jumps over a lazy dog'
for val in range(ord('a'),ord('z')+1):
    if chr(val) not in S:
        print('Not Panagram')
        break
else:
    print('Panagram')