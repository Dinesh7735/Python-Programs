num=int(input('Enter a number: '))
Sum=0
dup=num
while num>0:
    rem=num%10
    Sum=Sum+rem
    num=num//10
print(f'Sum of each digits in {dup} is {Sum}')
