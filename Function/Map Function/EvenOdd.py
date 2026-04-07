def EvenOdd(num):
    if num % 2 == 0:
        return f'{num} is Even'
    return f'{num} is Odd'
for ans in map(EvenOdd,range(1,11)):
    print(ans)