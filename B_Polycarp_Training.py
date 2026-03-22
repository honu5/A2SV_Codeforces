n=int(input())
lst=list(map(int,input().split()))
lst.sort()
val=0
for i in lst:
    if i>val:
        val+=1
print(val)
    