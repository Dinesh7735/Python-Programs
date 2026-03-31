# A program to print the least factor among 2,3,5 and 7 for given number
num=int(input('Enter the number: '))
if num%2==0:
    print(f'{num} is divisible by 2')
elif num%3==0:
    print(f'{num} is divisible by 3')
elif num%5==0:
    print(f'{num} is divisible by 5')
elif num%7==0:
    print(f'{num} is divisible by 7')
else:
    print(f'{num} has no factors')