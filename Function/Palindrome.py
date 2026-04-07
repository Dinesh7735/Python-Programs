def Palindrome(num,rev = 0):
    dup = num
    while num > 0:
        rem = num % 10
        rev = rev*10 + rem
        num //= 10
    if dup == rev:
        return 'Palindrome Number'
    return 'Not Palindrome Number'
print(Palindrome(12321))
print(Palindrome(123))