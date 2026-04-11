t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    d=list(map(int,input().split()))
    a=list(map(int,input().split()))
    if sum(a)>k:
        print(-1)
        continue
    def isPossible(x):
        total=0
        for i in range(n):
            trip=(d[i]+x-1)//x
            total+=trip*a[i]
        if total>k:
            return False
        return True
    l,r=1,max(d)+1
    while l<=r:
        mid=(l+r)//2
        if isPossible(mid):
            ans=mid
            r=mid-1
        else: l=mid+1
    print(ans)


