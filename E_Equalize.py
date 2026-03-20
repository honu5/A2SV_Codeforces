import sys
from collections import Counter

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))

    cnt = Counter()

    for i, x in enumerate(a):
        cnt[x - i] += 1

    print(max(cnt.values()))
