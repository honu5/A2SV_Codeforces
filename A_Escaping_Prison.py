t=int(input())
for i in range(t):
    n,height=map(int,input().split())
    val=0
    for i in range(n):
        w,l=map(int,input().split())
        val+=max(w,l)
    if val>=height:
        print("YES")
    else:        print("NO")