n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr = [(arr[i], i+1) for i in range(n)]
arr.sort()

total = 0
selected = []

for cost, idx in arr:
    if total + cost <= k:
        total += cost
        selected.append(idx)
    else:
        break

selected.sort()

print(len(selected))
for i in selected:
    print(i, end=' ')