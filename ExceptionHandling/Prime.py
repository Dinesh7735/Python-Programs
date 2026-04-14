try:
    num = 12
    if num > 1:
        for val in range(2,int(num**0.5)+1):
            if num % val == 0:
                raise Exception
    else:
        raise Exception
except Exception:
    print('Not a prime number')
else:
    print('Prime number')
