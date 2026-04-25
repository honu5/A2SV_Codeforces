t=int(input())
for i in range(t):
    correct="314159265358979323846264338327"
    val=0
    trial=input().strip()
    for i in range(len(trial)):
        if trial[i]==correct[i]:
            val+=1
        else: break
    print(val)
            