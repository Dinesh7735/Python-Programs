num = 11
if len([val for val in range(1,num+1) if num % val == 0]) == 2:
    print('Prime number')
else:
    print('Not a prime number')