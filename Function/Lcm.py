def Lcm(num1,num2):
    if num1 > num2:
        lcm = num1
    else:
        lcm = num2
    for val in range (lcm,num1*num2+1):
        if val % num1 == 0 and val % num2 == 0:
            return val
print(Lcm(2,5))