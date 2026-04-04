t = int(input())
for i in range(t):
    n = int(input())
    s = input().strip()
    gotIt = False
    for i in range(1, n):
        arr = [s[:i]]
        j = i        
        while j < n:
            num = ""            
            while j < n:
                num += s[j]
                j += 1                
                if len(num) > len(arr[-1]) or (len(num) == len(arr[-1]) and num > arr[-1]):
                    break            
            arr.append(num)       
             
        val = True
        for k in range(len(arr) - 1):
            a, b = arr[k], arr[k+1]
            if not (len(b) > len(a) or (len(b) == len(a) and b > a)):
                val = False
                break        
        if val and len(arr) >= 2:
            print("YES")
            print(len(arr))
            print(*arr)
            gotIt = True
            break    
    if not gotIt:
        print("NO")