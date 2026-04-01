num=int(input('Enter a number: '))
place=1
temp=num
Bin=0
while num>0:
    rem=num%2
    Bin=Bin+rem*place
    num//=2
    place*=10
print(f'Binary value of {temp} is {Bin}')