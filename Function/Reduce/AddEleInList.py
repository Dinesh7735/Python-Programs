import functools
print(functools.reduce(lambda n1,n2 : n1+n2,[10,20,30,40,50],0)) #0 isdefault value here it is given to avoid the error 