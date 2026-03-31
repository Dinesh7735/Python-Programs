#Greatest among 3 numbers
num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
num3=int(input("Enter 3rd number: "))
if num1>num2:
    if num1>num3:
        print(f"{num1} is greater")
    else:
        print(f"{num3} is greater")
else:
    if num2>num3:
        print(f'{num2} is greater')
    else:
        print(f'{num3} is greater')