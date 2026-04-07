def palindrome(num,rev=0):
    dup = num
    while num > 0:
        rem = num % 10
        rev = rev*10 + rem
        num //= 10
    if dup == rev:
        return 1
    return 0
def prime(num):
    if num > 1:
        for val in range(2,int(num**0.5)+1):
            if num % val == 0:
                return 0
        return 1
    return 0
def palyprime (num):
    if palindrome(num) and prime(num):
        return 'Palyprime'
    return 'Not Palyprime'

print(palyprime(11))
