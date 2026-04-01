num=int(input('Enter any number'))
dup=num
Sum=0
while num>0:
    rem=num%10
    fact=1
    while rem>0:
        fact*=rem
        rem-=1
    Sum+=fact
    num//=10
if Sum==dup:
    print(f'{dup} is a strong number')
else:
    print(f'{dup} is not a strong number')