def Palindrome(num):
    place = 10**(len(str(num))-1)
    if num == 0:
        return 0
    return (num % 10)*place + Palindrome(num // 10)
num = 121
if Palindrome(num) == num:
    print('Palindrome')
else:
    print('Not Palindrome')