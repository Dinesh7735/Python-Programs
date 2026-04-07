def EvenOdd(num):
    if num % 2 == 0:
        return True
    return False
print(list(filter(EvenOdd,range(1,7))))