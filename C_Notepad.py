n=int(input())
for i in range(n):
    a=int(input())
    b=input().strip()
    found=False
    for i in range(len(b)-1):
        if b[i:i+2] in b[i+2:]:
            print("YES")
            found=True
            break
    if not found:
        print("NO")