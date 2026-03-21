arr=list(map(int,input().split()))
n=arr[0]
k=arr[1]
cakes=list(input().strip())
cakes.sort()
ans=[cakes[0]]  
val=ord(cakes[0]) - 96  
i=1   
while i<n and len(ans)<k:
    if ord(ans[-1]) + 1 < ord(cakes[i]):   
        ans.append(cakes[i])
        val += ord(cakes[i]) - 96
    i+=1
if len(ans) < k:
    print(-1)
else:
    print(val)