def Bin_To_Int(num,power = 0):
    if num == 0:
        return 0
    return (num % 10)*(2**power) + Bin_To_Int(num // 10,power + 1)
num = 101
print(Bin_To_Int(num))