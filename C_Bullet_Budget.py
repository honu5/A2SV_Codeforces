t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))
    monsters = []
    for i in range(n):
        monsters.append((abs(x[i]), a[i]))
    monsters.sort()
    totHlth = 0
    possible = True
    for dist, health in monsters:
        totHlth += health
        blts = dist * k

        if totHlth > blts:
            possible = False
            break
    if possible:
        print("YES")
    else:
        print("NO")