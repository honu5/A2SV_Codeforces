arr = list(map(int, input().split()))
n = arr[0]
k = arr[1]

lst = list(map(int, input().split()))
lst.sort()
if k == n:
    print(0)
else:
    total= lst[-1]-lst[0]
    diff=[]
    for i in range(1,len(lst)):
        diff.append(lst[i]-lst[i-1])
    diff.sort(reverse=True)
    for i in range(k-1):
        total-=diff[i]
    print(total)