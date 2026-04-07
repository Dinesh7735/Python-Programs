def Happy(num):
    while num > 9:
        num = square(num)
    return num == 1 or num == 7
def square(num,Sum = 0):
    while num > 0:
        Sum += (num % 10) ** 2
        num //= 10
    return Sum
print(list(filter(Happy,range(1,11))))