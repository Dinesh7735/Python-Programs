num1=int(input('Enter 1st number: '))
num2=int(input('Enter 2nd number: '))
if num1>num2:
    lcm=num1
else:
    lcm=num2
for lcm in range(lcm,num1*num2+1):
    if lcm%num1==0 and lcm%num2==0:
        print(lcm)
        break