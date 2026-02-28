t=int(input())

for i in range(t):
    val=0

    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    for i in range(0,len(arr),2):
        val+=arr[i]
    print(val)