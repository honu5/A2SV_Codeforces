n=int(input())
arr=list(map(int,input().split()))
if max(arr)<=25:
    print(0)
else:  print(max(arr)-25)