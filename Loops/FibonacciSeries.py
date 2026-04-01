n=int(input('Enter the nth term: '))
t1=0
t2=1
for val in range(n):
    print(f'{t1},',end=' ')
    t1,t2 = t2,t1+t2    

   

