t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    p = list(map(int, input().split()))
    
    cur = 0
    
    for i in range(1, n):
        remaining = h[i] - cur * p[i-1]
        if remaining > 0:
            cur += (remaining + p[0] - 1) // p[0]
    
    print(cur)