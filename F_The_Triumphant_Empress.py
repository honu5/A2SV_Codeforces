import bisect

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    A = list(map(int, input().split()))    
    queries = [[] for _ in range(n)]
    for idx in range(q):
        k, x = map(int, input().split())
        queries[k-1].append((x, idx))    
    ans = [0] * q
    sorted_list = []
    
    for i in range(n):      
        bisect.insort(sorted_list, A[i])        
        for x, idx in queries[i]:
            cnt = bisect.bisect_left(sorted_list, x) 
            ans[idx] = cnt
    
    for x in ans:
        print(x)