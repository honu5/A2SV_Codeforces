
from collections import Counter
from random import randint
t=int(input())
for i in range(t):
    arr=list(map(int,input().split()))
    shelf=arr[0]
    juice=arr[1]
    juices=[]
    for j in range(juice):
        juices.append(list(map(int,input().split())))
    cnt=Counter()
    for k in juices:
        cnt[k[0]^randint(1, 1000000)]+=k[1]
    cnt=sorted(cnt.items(),key=lambda x: x[1],reverse=True)
    i=0
    total=0
    while i<shelf and i<len(cnt): 
        total+=cnt[i][1]
        i+=1
    print(total)
