t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    p = [0]*n
    i = 0
    pos= True
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        if j - i == 1:
            pos = False
            break
        for k in range(i, j-1):
            p[k] = k + 2
        p[j-1] = i + 1
        i = j
    if not pos:
        print(-1)
    else:
        print(*p)