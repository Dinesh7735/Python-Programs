S = 'the quick brown fox jumps over a lazy dog'
val = ord('a')
while val <= ord('z'):
    if chr(val) not in S:
        print('Not Panagram')
        break
    val += 1
else:
    print('Panagram')