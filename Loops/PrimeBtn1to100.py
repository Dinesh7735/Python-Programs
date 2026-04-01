for val in range(1,101):
    count=0
    for val2 in range(1,val+1):
        if val%val2==0:
            count+=1
    if count==2:
        print(val)