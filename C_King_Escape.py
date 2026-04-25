from collections import deque
n = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())
dirs = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
def safe(x, y):
    if x < 1 or x > n or y < 1 or y > n:
        return False
    if x == ax or y == ay:
        return False
    if abs(x - ax) == abs(y - ay):
        return False
    return True
visited = set()
q = deque()
q.append((bx, by))
visited.add((bx, by))

possible = False

while q:
    x, y = q.popleft()
    if (x, y) == (cx, cy):
        possible = True
        break
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if (nx, ny) not in visited and safe(nx, ny):
            visited.add((nx, ny))
            q.append((nx, ny))
if possible:
    print("YES")
else:
    print("NO")