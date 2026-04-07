def RemoveWord(l,w):
    n = []
    for i in l:
        if i!=w:
            n.append(i.strip(w))
    return n
L=['Ahan','Amar','Aman','an']
W='an'
print(f"{RemoveWord(L,W)}")

