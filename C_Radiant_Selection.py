import math

t = int(input())
for i in range(t):
    k = int(input())    
    left, right = 1, 2*k   
    while left < right:
        mid = (left + right) // 2
        if mid - int(math.isqrt(mid)) >= k:
            right = mid
        else:
            left = mid + 1    
    print(left)