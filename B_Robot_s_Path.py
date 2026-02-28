lst=list(map(int,input().split()))
string=input().strip()
check=["#"]*lst[1]
if "".join(check) in string:
    print("NO")
else:   print("YES")
