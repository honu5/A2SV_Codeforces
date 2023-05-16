t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    found=False
    for i in range(n):
        if arr[arr[i]-1]==i+1:
            print(2)
            found=True
            break
    if not found:
        print(3)