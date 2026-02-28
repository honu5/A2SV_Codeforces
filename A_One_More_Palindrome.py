from collections import Counter
t = int(input())
for i in range(t):
    val=0
    s = input().strip()
    
    freq = Counter(s)
    
    for j in freq.values():
        if j//2>1:
            val+=1
    
    if val>= 2:
        print("YES")
    else:
        print("NO")