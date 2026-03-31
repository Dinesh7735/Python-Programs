import copy
l = [[1,2],[4,5]]
dup = copy.deepcopy(l)
print(l is dup)
print(l[0] is dup[0])
print(l[0][1] is dup[0][1])
