t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr1=sorted(arr)
    if arr[-1]>=max(arr):
        print(arr1[-2]+max(arr))
    else: print(max(arr)+arr[-1])
    