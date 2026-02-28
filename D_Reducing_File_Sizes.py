arr=list(map(int,input().split()))
n,total=arr[0],arr[1]
lst=[]
for i in range(n):
    lst.append(list(map(int,input().split())))
lst.sort(key=lambda x: abs(x[0]-x[1]),reverse=True)
i=0
curr=sum(x[0] for x in lst)
while curr>total and i<n:
    curr-=abs(lst[i][0]-lst[i][1])
    i+=1
if curr>total:   print(-1)
else:
    print(i)