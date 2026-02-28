n=int(input())
for i in range(n):
    s=int(input())
    alice=1
    bob=0
    i=2
    summ=1
    bobs=True
    while summ<s:
        
        if bobs:
            bob+=(i+i+1)
            bobs=False
        else:
            alice+=(i+i+1)
            bobs=True
        summ+=i+i+1
        i+=2
    if summ>s:
        if bobs:
            alice-=(summ-s)
        else:
            bob-=(summ-s)
    print(alice,bob)
        



