num=int(input('Enter the number: '))
dup=num
sum=0
power=len(str(num))
while num>0:
    rem=num%10
    sum=sum+rem**power
    power-=1
    num=num//10
if dup==sum:
    print(f'{dup} is disarum number')
else:
    print(f'{dup} is not disarum number')
