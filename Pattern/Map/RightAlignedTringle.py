num = 5
print('\n'.join(list(map(lambda val : '  '*(num-val) + '* '* val,range(1,num+1)))))