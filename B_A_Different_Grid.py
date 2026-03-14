t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    ans= []
    flat = []

    for j in range(n):
        row = list(map(int, input().split()))
        ans.append(row)
        flat.extend(row)

    if n * m == 1:
        print(-1)
        continue
    flat = flat[1:] + flat[:1]
    idx = 0
    for i in range(n):
        for j in range(m):
            print(flat[idx], end=" ")
            idx += 1
        print()