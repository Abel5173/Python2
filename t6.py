#code
t = int(input())
while t > 0:
    n = int(input())
    l = [int(x) for x in input().split()]
    l = l[::-1]
    x = 0
    s = 0
    n -= 1
    while x <= n:
        if x%2 == 0:
            s += (l[n-x])**2
        else:
            s -= (l[n-x])**2
        x+=1
    print(abs(s))
    
    t-=1