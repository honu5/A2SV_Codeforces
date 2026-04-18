t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    i=1
    while k>0 and i<n:
        val=(arr[i-1]-arr[i])
        val2=min(k,val)
        arr[i]+=val2
        k-=val2
        i+=2
    
    
    A=0
    B=0
    for i in range(n):
        if i%2==0:
            A+=arr[i]
        else:
            B+=arr[i]
    print(A-B)