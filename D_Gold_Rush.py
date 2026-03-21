def possible(n, m):
    if n == m:
        return True
    if n < m:
        return False
    if n % 3 != 0:
        return False
    
    return possible(n / 3, m) or possible(2 * n / 3, m)

t = int(input())
for i in range(t):
    arr=list(map(int, input().split()))
    n=arr[0]
    m=arr[1] 
    if possible(n, m):
        print("YES")

    else:
        print("NO")