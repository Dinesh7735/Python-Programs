num=int(input('Enter the number: '))
dup = num
rev=0
while num>0:
    rem = num%10
    rev = rev*10+rem
    num = num//10
if dup==rev:
    print(f'{dup} is palindrome')
else:
    print(f'{dup} is not palindrome')