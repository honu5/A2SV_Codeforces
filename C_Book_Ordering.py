n=int(input())
lst=list(map(int,input().split()))
prev=max(lst[0],lst[1])
found=True
for i in range(1,n):
    lst=list(map(int,input().split()))
    lrg=max(lst[0],lst[1])
    sml=min(lst[0],lst[1])
    if lrg<=prev:
        prev=lrg
    elif sml<=prev:
        prev=sml
    else:
        print("NO")
        found=False
        break
if found:    print("YES")
    
    



