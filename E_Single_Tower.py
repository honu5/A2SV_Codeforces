n = int(input())
blocks = []
pos = {}

for tower_id in range(n):
    data = list(map(int, input().split()))
    k = data[0]
    arr = data[1:]
    for idx, val in enumerate(arr):
        blocks.append(val)
        pos[val] = (tower_id, idx)

blocks.sort()
good = 0

for i in range(len(blocks) - 1):
    a = blocks[i]
    b = blocks[i + 1]
    t1, p1 = pos[a]
    t2, p2 = pos[b]
    if t1 == t2 and p2 == p1 + 1:
        good += 1

N = len(blocks)
segments = N - good

splits = segments - n
if splits < 0:
    splits = 0

combines = segments - 1

print(splits, combines)