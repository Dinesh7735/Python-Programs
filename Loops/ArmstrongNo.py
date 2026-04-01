num=int(input('Enter the number: '))
dup=num
sum=0
power=len(str(num))
while num>0:
    rem=num%10
    sum=sum+rem**power
    num=num//10
if dup==sum:
    print(f'{dup} is armstrong')
else:
    print(f'{dup} is not armstrong')
