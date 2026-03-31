def Fibo(n):
    if n <= 0:
        return 'No Value'
    if n == 1 or n == 2:
        return n-1
    return Fibo(n-1) + Fibo(n-2)
print(Fibo(5))