t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    
    wins = 0
    left = 0
    total = 0
    
    for right in range(n):
        total += a[right]
        
        while total > r and left <= right:
            total -= a[left]
            left += 1
        
        if l <= total <= r:
            wins += 1
            total = 0
            left = right + 1
    
    print(wins)