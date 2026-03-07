import bisect
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    gd = []
    ans = 0
    for j in range(1,n+1):
        if a[j-1] < j:
            pos = bisect.bisect_left(gd, a[j-1])
            ans += pos
            gd.append(j)
    print(ans)