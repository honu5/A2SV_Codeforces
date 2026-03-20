from collections import Counter
from random import randint

t = int(input())

for i in range(t):
    shelf, juice = map(int, input().split())
    rand = randint(1, 10**9)
    cnt = Counter()

    for _ in range(juice):
        a, b = map(int, input().split())
        cnt[a ^ rand] += b
    cnt = sorted(cnt.values(), reverse=True)

    total = 0
    for i in range(min(shelf, len(cnt))):
        total += cnt[i]

    print(total)
