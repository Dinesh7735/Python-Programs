num = 5
print('\n'.join(list(map(lambda val : '  '*(num-val) + '* '*val,range(num,0,-1)))))