t = int(input())
for i in range(t):
    n = int(input())
    s = input().strip()
    odd = 0
    ans = -1
    for i in range(n):
        if int(s[i]) % 2 == 1:
            odd += 1
        if odd % 2 == 0 and int(s[i]) % 2 == 1:
            ans = s[:i+1]
            break
    print(ans)