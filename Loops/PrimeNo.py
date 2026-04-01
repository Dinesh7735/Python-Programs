num=int(input('Enter a number: '))
count=0
for val in range(1,num+1):
    if num%val==0:
        count+=1
if count==2:
    print(f'{num} is prime')
else:
    print(f'{num} is not prime')