
t = int(input())
ALPH = ['0', '2', '5', '6']
PAT = "2025"
M = len(PAT)
INF = 10**9

pi = [0] * M
j = 0
for i in range(1, M):
    while j > 0 and PAT[i] != PAT[j]:
        j = pi[j - 1]
    if PAT[i] == PAT[j]:
        j += 1
    pi[i] = j

def next_state(state, ch):
    while state > 0 and (state == M or PAT[state] != ch):
        state = pi[state - 1]
    if PAT[state] == ch:
        state += 1
    return state

nxt = [[0] * 4 for _ in range(M + 1)]
for st in range(M + 1):
    for idx, c in enumerate(ALPH):
        nxt[st][idx] = next_state(st, c)

for _ in range(t):
    n = int(input().strip())
    s = input().strip()

    target = "2026"
    cost_yes2026 = INF
    for i in range(n - 3):
        mism = 0
        for k in range(4):
            if s[i + k] != target[k]:
                mism += 1
        cost_yes2026 = min(cost_yes2026, mism)

    dp = [INF] * (M + 1)
    dp[0] = 0

    for i in range(n):
        ndp = [INF] * (M + 1)
        for st in range(M):  
            if dp[st] == INF:
                continue
            base = dp[st]
            for idx, c in enumerate(ALPH):
                nst = nxt[st][idx]
                if nst == M:
                    continue  
                cost = base + (c != s[i])
                if cost < ndp[nst]:
                    ndp[nst] = cost
        dp = ndp

    cost_no2025 = min(dp[:M])

    print(min(cost_yes2026, cost_no2025))
