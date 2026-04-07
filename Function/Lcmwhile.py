def Lcm(num1,num2):
    if num1 > num2:
        lcm = num1
    else:
        lcm = num2
    while True:
        if lcm % num1 == 0 and lcm % num2 == 0:
            return lcm
        lcm += 1
print(Lcm(2,5))
