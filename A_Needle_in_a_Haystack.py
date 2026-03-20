t=int(input())
for i in range(t):
    s=input().strip()
    t=input().strip()
    s=list(s)
    t=list(t)
    
    for i in s:
        if i in t:
            t.remove(i)
        else:
            print("Impossible")
            break
    else:
        t.sort()
        if t[-1]<=s[0]:
            t.extend(s)
        else:
            for i in range(len(t)-1):
                if s[0]<t[i+1]:
                    t[i:i]=s
                    break
    
            print("".join(t))
    