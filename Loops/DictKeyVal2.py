# A program to access key value pair from dictionary using varN.items()
D = {5:45,'123':[22,33,44],False:2345,(3+9j):420}
for key,val in D.items():
    print(f'{key} : {val}')