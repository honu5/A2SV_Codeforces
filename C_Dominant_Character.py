t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    ans = float('inf')

    for i in range(n):
        a = b = c = 0
        for j in range(i, min(n, i + 7)):
            if s[j] == 'a':
                a += 1
            elif s[j] == 'b':
                b += 1
            else:
                c += 1

            length = j - i + 1

            if length >= 2 and a > b and a > c:
                ans = min(ans, length)

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)