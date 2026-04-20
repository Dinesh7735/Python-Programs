L = [12,33,45,76,34,67,87,34,23,33]
L.sort()
res = []
for ele in L:
    if ele not in res:
        res.append(ele)
target = 33
least = 0
high = len(res) - 1
while least <= high and res[least] <= target <= res[high]:
    mid = int(least + ((high - least) / (res[high] - res[least]))*(target - res[least]))
    if res[mid] > target:
        high = mid - 1
    elif res[mid] < target:
        least = mid + 1
    else:
        print(mid)
        break
else:
    print(-1)