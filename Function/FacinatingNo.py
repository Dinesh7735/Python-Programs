def Facinating(num):
    S = str(num*1) + str(num*2) + str(num*3)
    for val in range(1,10):
        if str(val) not in S:
            return 'Not a Facinating Number'
    return 'Facinating Number'
print(Facinating(192))
print(Facinating(193))