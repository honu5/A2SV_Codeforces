n=int(input())
word=input().strip()
val=0
res=[]
for i in range(n):
    if len(res)%2==0:
        res.append(word[i])
    else:
        if word[i] !=res[-1]:
            res.append(word[i])
        else:
            val+=1
            continue
print(val)
print("".join(res))