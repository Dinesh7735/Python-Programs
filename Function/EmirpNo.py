def palindrome(num):
    global rev
    rev = 0
    dup = num
    while num > 0:
        rem = num % 10
        rev = rev*10 + rem
        num //= 10
    return dup != rev
def prime(num):
    if num > 1:
        for val in range(2,int(num**0.5)+1):
            if num % val == 0:
                return 0
        return 1
def Emirp(num):
    if palindrome(num) and prime(num) and prime(rev):
        return 'Emirp No'
    return 'Not Emirp'
print(Emirp(13))