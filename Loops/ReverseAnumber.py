num=int(input('Enter a number: '))
dup = num
rev = 0
while num>0:
    rem = num%10
    rev = rev*10+rem
    num = num//10
print(f'reverse of {dup} is {rev}')