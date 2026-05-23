t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    if n%2==0:
        found=False
        for i in range(1,n,2):
            if int(s[i])%2==0:
                found=True
                print(2)
                break
        if not found:
            print(1)
    if n%2!=0:
        found=False
        for i in range(0,n,2):
            if int(s[i])%2==1:
                found=True
                print(1)
                break
        if not found:
            print(2)

