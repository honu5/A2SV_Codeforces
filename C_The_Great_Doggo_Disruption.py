from collections import Counter
length=int(input())

string=input().strip()
cnt=Counter(string)
most=cnt.most_common()
if len(string)==1:
    print("Yes")
elif most[0][1]>=2:
    print("Yes")
else:
    print("No")