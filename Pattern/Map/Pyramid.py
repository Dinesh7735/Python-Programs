num = 5
print('\n'.join(list(map(lambda val : '  '*(num-val) + '* '*(2*val-1),range(1,num+1)))))