class Strong(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg
try:
    num = 145
    dup = num
    Sum = 0
    while num > 0:
        rem = num % 10
        fact = 1
        for val in range(1,rem+1):
            fact *= val
        Sum += fact
        num //= 10
    if dup != Sum:
        raise Strong('Not a strong number')
except Strong as msg:
    print(msg)
else:
    print('Strong number')