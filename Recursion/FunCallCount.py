def Sample(num):
    print(num)
    num += 1
    Sample(num)
num = 1
Sample(num) #If there is no termination condition, a recurssive function calls itself 2^10 = 1024 times
#But here the Sample function is calling itself 997 times because some of the stack memory is used by the 
#variable which we have used in the program