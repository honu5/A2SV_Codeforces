n = int(input())
for i in range(n):
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]

    layers = min(n, m) // 2
    total = 0

    for layer in range(layers):
        top = layer
        bottom = n - layer - 1
        left = layer
        right = m - layer - 1

        s = ""

        for j in range(left, right + 1):
            s += grid[top][j]
        for i in range(top + 1, bottom):
            s += grid[i][right]
        for j in range(right, left - 1, -1):
            s += grid[bottom][j]
        for i in range(bottom - 1, top, -1):
            s += grid[i][left]
        s += s[:3]

        for i in range(len(s) - 3):
            if s[i:i+4] == "1543":
                total += 1

    print(total)
