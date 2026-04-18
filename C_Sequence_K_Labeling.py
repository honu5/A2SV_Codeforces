from collections import Counter
n,k=map(int,input().split())
arr=list(map(int,input().split()))
count=Counter(arr)
most=count.most_common(1)[0][1]
if most>k:
    print("NO")
else:
    print("YES")
    b = [(val, i) for i, val in enumerate(arr)]
    b.sort()

    res = [0] * n

    for i in range(n):
        _,idx = b[i]
        res[idx] = (i % k) + 1

    print(*res)


