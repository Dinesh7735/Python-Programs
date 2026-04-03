# A program to print pair of element whose sum is equal to the target [7].
L = [5,4,6,3,1,0]
target = 7
for ele1 in range(len(L)-1):
    for ele2 in range(ele1+1,len(L)):
        if L[ele1] + L[ele2] == target:
            print(f'({L[ele1]}, {L[ele2]})')