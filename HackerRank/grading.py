n = int(input())
l = []
m = []
for i in range(n):
    l.append(int(input()))
for i in l:
    if i < 38:
        print(i)
    elif i%5 < 5 and 5-i%5 < 3:
        print(i - (i%5) + 5)
    elif i%5 > 5 and 5-i%5 < 3:
        print(i - (i%5) + 10)
    else:
        print(i)
