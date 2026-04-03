L = [5, 4, 10, 6, 3, 1, 0]
ind1 = 0
target = 7
while ind1 < len(L)-1:
    ind2 = ind1 + 1
    while ind2 < len(L):
        if L[ind1] + L[ind2] == target:
            print(f'({L[ind1]}, {L[ind2]})')
        ind2 += 1
    ind1 += 1