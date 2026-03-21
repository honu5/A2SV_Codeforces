arr=list(map(int,input().split()))
a,b=arr[0],arr[1]
if b%2==1 and str(b)[-1]!='1':
    print("NO")
else:
    path = [b] 
    while a<b:
        if b % 10 == 1:
            b = (b - 1) // 10
            path.append(b)
        elif b % 2 == 0:
            b //= 2
            path.append(b)
        else:
            print("NO")
            break
    else:
        if a == b:
            print("YES")
            path.reverse()   
            print(len(path))
            print(*path)
        else:
            print("NO")