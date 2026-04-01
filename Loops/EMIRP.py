num = int(input('Enter a number: '))
temp = num
rev = 0
count1 = 0
count2 = 0
for val in range(1,num+1):
    if num % val == 0:
        count1 += 1
if count1 == 2:
    while num > 0:
        rem = num%10
        rev = rev*10+rem
        num //=10
    if temp != rev:
        for val in range(1,rev+1):
            if rev % val == 0:
                count2 += 1
        if count2 == 2:
            print(f'{temp} is an EMIRP number')
        else:
            print(f'{temp} is not an EMIRP number')
    else:
        print(f'{temp} is not an EMIRP number')
else:
    print(f'{temp} is not an EMIRP number')
        
