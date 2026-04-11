t=int(input())
for i in range(t):
    n,m=list(map(int,input().split()))
    s=input().strip()
    w=input().strip()
    tar=sum(ord(c)-ord('a') for c in w)
    curr=sum(ord(c)-ord('a') for c in s[:m])
    if curr==tar:
        print("YES")
        continue
    found=False
    for i in range(m,n):
        curr+=ord(s[i])-ord('a')
        curr-=ord(s[i-m])-ord('a')
        if curr==tar:
            print("YES")
            found=True
            break
    if not found:
        print("NO")