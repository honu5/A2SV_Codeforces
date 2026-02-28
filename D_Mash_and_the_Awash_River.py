import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

t = int(input())

def solve(s):
    n = len(s)
    vis = [0] * n      
    dp = [0] * n      
    infinite = False

    def dfs(u):
        nonlocal infinite
        if u < 0 or u >= n:
            return 0
        if vis[u] == 1:
            infinite = True
            return 0
        if vis[u] == 2:
            return dp[u]

        vis[u] = 1
        best = 0

        if s[u] == '<':
            best = dfs(u - 1)
        elif s[u] == '>':
            best = dfs(u + 1)
        else:  # '*'
            best = max(dfs(u - 1), dfs(u + 1))

        vis[u] = 2
        dp[u] = best + 1
        return dp[u]

    ans = 0
    for i in range(n):
        if vis[i] == 0:
            dfs(i)
        if infinite:
            return -1
        ans = max(ans, dp[i])

    return ans

for _ in range(t):
    s = input().strip()
    print(solve(s))
