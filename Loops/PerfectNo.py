num=int(input('Enter a number: '))
dup=num
s=0
for val in range(1,num):
    if num%val==0:
        s+=val
if dup==s:
    print(f'{dup} is a perfect number')
else:
    print(f'{dup} is not a perfect number')