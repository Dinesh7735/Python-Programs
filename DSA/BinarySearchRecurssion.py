def Binary(L,target,least,high,mid):
    if least > high:
        return -1
    if L[mid] > target:
        return Binary(L,target,least,mid-1,(least + (mid-1))//2)
    if L[mid] < target:
        return Binary(L,target,mid+1,high,((mid+1) + high)//2)
    return mid
    
L = [12,33,45,76,34,67,87,34,23,33]
target  = 34
L.sort()
res = []
for ele in L:
    if ele not in res:
        res.append(ele)

least = 0
high = len(res) - 1
mid = (least + high) // 2
print(f'Result - {res} \nTarget - {target}')
print(Binary(res,target,least,high,mid))