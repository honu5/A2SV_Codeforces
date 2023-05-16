t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    a, b = arr[0], arr[1]
    
    ans = 10**18
    
    for x in range(31):
        if b == 1 and x == 0:
            continue
        
        nb = b + x
        ta = a
        cnt = 0
        
        while ta > 0:
            ta //= nb
            cnt += 1
        
        ans = min(ans, x + cnt)
    
    print(ans)