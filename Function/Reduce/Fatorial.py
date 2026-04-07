import functools
num = 5
print(functools.reduce(lambda n1,n2 : n1*n2,range(1,num+1),1))