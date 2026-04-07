def Fibonacci(n):
    t1,t2 = 0,1
    for val in range (n):
        print(t1, end=' ')
        t1,t2 = t2,t1+t2


n = int(input('Enter the number of term: '))
Fibonacci(n)
