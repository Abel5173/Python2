try:
    while True:
        n = int(input())
        d = 0
        l = [1, 3, 4, 5, 7, 9]
        if n in l:
            print(l.index(n))
        else:
            a = len(str(n))
            if n % 10 == [3, 4, 5]:
                for i in range(a+1):
                    d += ((n%10) * (6**i))
                    n = int(n/10)
                d -= (8*(10**(a-2)))
                print(d)
            elif n%10 == 9:
                for i in range(a+1):
                    d += ((n%10) * (6**i))
                    n = int(n/10)
                d -= (10*(10**(a-2)))
                print(d)
            elif n%10 == 7:
                for i in range(a+1):
                    d += ((n%10) * (6**i))
                    n = int(n/10)
                d -= (9*(10**(a-2)))
                print(d)
            elif n%10 == 1:
                for i in range(a+1):
                    d += ((n%10) * (6**i))
                    n = int(n/10)
                d -= (7*(10**(a-2)))
                print(d)
except:
    pass
