t = int(input())

for _ in range(t):
    n,m,v = map(int,input().split())
    a = list(map(int,input().split()))
    pref=[0]*(n+1)
    s=0
    cnt=0
    for i in range(n):
        s+=a[i]
        if s>=v:
            cnt+=1
            s=0
        pref[i+1]=cnt
    suf=[0]*(n+2)
    s=0
    cnt=0
    for i in range(n-1,-1,-1):
        s+=a[i]
        if s>=v:
            cnt+=1
            s=0
        suf[i]=cnt

    if pref[n] < m:
        print(-1)
        continue
    ps=[0]*(n+1)
    for i in range(n):
        ps[i+1]=ps[i]+a[i]

    ans=0
    l=0
    for r in range(n):
        while l<=r and pref[l]+suf[r+1] >= m:
            ans=max(ans, ps[r+1]-ps[l])
            l+=1
    print(ans)