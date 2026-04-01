num = int(input('Enter the number: '))
dup = num
rev = 0
count = 0
for val in range (1,num+1):
    if num % val == 0:
        count += 1
if count == 2:
    while num > 0:
        rem = num%10
        rev = rev*10+rem
        num //=10
    if dup == rev:
        print(f'{dup} is palyprime')
    else:
        print(f'{dup} is not a palyprime')
else:
    print(f'{dup} is not a palyprime')