t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    # check if all characters same
    if len(set(s)) == 1:
        print(n)
        continue
    
    l, r = 0, n - 1
    
    while l < r and s[l] == s[r]:
        l += 1
        r -= 1
    
    print(r - l + 1)