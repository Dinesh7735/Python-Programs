def Palyprime(num,rev = 0):
    dup = num
    while num > 0:
        rem = num % 10
        rev = rev*10+rem
        num //= 10
    if dup == rev and prime(dup):
        return 'Palyprime'
    return 'Not a Palyprime'

def prime(num):
    if num > 1:
        for val in range(2,int(num**0.5)+1):
            if num % val == 0:
                return False
        return True
    
print(Palyprime(11))
