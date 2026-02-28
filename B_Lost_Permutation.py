n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))

    current_sum = sum(c)
    total_needed = current_sum + b

    k = max(c)

    while k * (k + 1) // 2 < total_needed:
        k += 1

    if k * (k + 1) // 2 == total_needed:
        print("YES")
    else:
        print("NO")
