t=int(input())

for i in range(t):
    s=input().strip()
    p=int(input())
    vals=[]
    total=0
    for i in range(len(s)):
        v = ord(s[i]) - ord('a') + 1
        
        vals.append((v,i))
        total += v
    vals.sort(key=lambda x: x[0], reverse=True)
    removed=set()
    i=0
    while total>p:


        v,idx = vals[i]
        total -= v
        removed.add(idx)

        i+=1

    ans=[]
    for i in range(len(s)):

        if i not in removed:
            ans.append(s[i])
    print("".join(ans))