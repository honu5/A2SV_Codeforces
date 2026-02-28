n = int(input())
for t in range(n):
    n = int(input())
    grid = [list(input().strip()) for _ in range(n)]

    moves = 0

    for i in range(n):
        for j in range(n):
            positions = [
                (i, j),
                (j, n-1-i),
                (n-1-i, n-1-j),
                (n-1-j, i)
            ]

            positions.sort()

            if (i, j) == positions[0]:
                ones = 0
                for x, y in positions:
                    if grid[x][y] == '1':
                        ones += 1
                moves += min(ones, 4 - ones)

    print(moves)
