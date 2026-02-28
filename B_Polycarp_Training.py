n=int(input())
lst=list(map(int,input().split()))
lst.sort()
val=0
if len(lst)==1 and lst[0]>=1:
    print(1)
else:
    i=0
    while i<len(lst):
        if lst[i]>=val:
            val+=1
            i+=1
        else:   
            i+=1
print(val)