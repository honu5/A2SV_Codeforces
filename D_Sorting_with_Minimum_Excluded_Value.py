t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))    
    ops = []   
    while True:
        srted = True
        for i in range(n):
            if a[i] != i:
                srted = False
                break
        if srted:
            break    
        present = [0] * (n + 1)
        for x in a:
            if x <= n:
                present[x] = 1    
        m = 0
        while present[m]:
            m += 1        
        if m < n:
            a[m] = m
            ops.append(m + 1)  
        else:
            for i in range(n):
                if a[i] != i:
                    a[i] = m
                    ops.append(i + 1)
                    break    
    print(len(ops))
    print(*ops)