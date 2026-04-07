def prime(num):
    if num > 1:
        for val in range(2,int(num**0.5)+1):
            if num % val == 0:
                return False
        return True
    
def reverse(num,Sum=0):
    while num > 0:
        Sum = Sum*10 + (num % 10) 
        num //= 10
    return Sum
def EMIRP(num):
    rev = reverse(num)
    if prime(num) and rev != num and prime(rev):
        return 'EMIRP No'
    return 'Not EMIRP No'
num = 113
print(EMIRP(num))