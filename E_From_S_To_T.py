q = int(input())

for _ in range(q):
    s = input().strip()
    t = input().strip()
    p = input().strip()

    i = 0
    for c in t:
        if i < len(s) and s[i] == c:
            i += 1
    if i != len(s):
        print("NO")
        continue
    from collections import Counter

    cs = Counter(s)
    ct = Counter(t)
    cp = Counter(p)

    ok = True
    for ch in ct:
        need = ct[ch] - cs.get(ch, 0)
        if need > cp.get(ch, 0):
            ok = False
            break

    print("YES" if ok else "NO")
