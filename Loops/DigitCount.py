num=int(input('Enter a number: '))
dup = num
count = 0
while num>0:
    count+=1
    num = num//10
print(f'Number of digits in {dup} is {count}')