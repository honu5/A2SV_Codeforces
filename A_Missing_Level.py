n=int(input())

lst=list(map(int,input().split()))
lst.sort()
for i in range(len(lst)):
    if lst[i]!=i+1:
        print(i+1)
        break