n = int(input())
l = [int(i) for i in input().split()]
x = l[n-1]
i = n-1
while i >= 0:
    if l[i-1] > x and i-1>=0:
        l[i] = l[i-1]
        print(*l)  
    elif i-1 == -1:
        l[0]=x
        print(*l)
        break
    else:
        l[i] = x
        print(*l)
        break
    i -= 1