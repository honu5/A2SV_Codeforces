t = int(input())
for i in range(t):
    n = int(input())
    enemy = list(input().strip())
    s = input().strip()
    ans = 0
    for j in range(n):
        if s[j] == '1':
            if j > 0 and enemy[j-1] == '1':
                ans += 1
                enemy[j-1] = '0'            
           
            elif enemy  [j] == '0':
                ans += 1                
            elif j < n-1 and enemy[j+1] == '1':
                ans += 1
                enemy[j+1] = '0'

    print(ans)