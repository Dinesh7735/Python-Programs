num=int(input('Enter a number: '))
dup=num
rev=0
power=10**(len(str(num))-1)
while num>0:
    rem=num%10
    rev=rev+rem*power
    num=num//10
    power=power//10
print(rev)
if dup==rev:
    print(f'{dup} is a palindrome number')
else:
    print(f'{dup} is not a palindrome number')