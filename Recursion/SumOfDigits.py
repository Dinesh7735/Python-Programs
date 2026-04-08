def Add_digits(num):
    if num == 0:
        return 0
    return (num % 10) + Add_digits(num // 10)
num = 567
print(Add_digits(num))