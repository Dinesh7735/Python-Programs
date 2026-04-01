num = int(input('Enter the number: '))
dup = num
rev = 0
count = 0
while num > 0:
    rem = num%10
    rev = rev*10+rem
    num //=10
if dup == rev:
    for val in range(1,dup+1):
        if dup % val == 0:
            count +=1
    if count == 2:
        print(f'{dup} is a palyprime')
    else:
        print(f'{dup} is not a paliprime')
else:
    print(f'{dup} is not a palyprime')