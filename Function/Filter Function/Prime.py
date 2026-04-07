def Prime(num):
    if num > 1:
        for val in range(2,int(num**0.5)+1):
            if num % val == 0:
                return False
        return True
    
print(list(filter(Prime,range(1,101))))