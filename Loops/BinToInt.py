num=1100
dup=num
power=0
Sum=0
while num>0:
    rem=num%10
    Sum=Sum+rem*(2**power)
    num//=10
    power+=1
print(f'integer value of {dup} is {Sum}')