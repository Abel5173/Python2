from math import atan, cos, pi, sin, tan

t = int(input())
for i in range(t):
    n, s = map(int, input().split())
    ang = (180 * (n - 2))/ (2 * n)
    ang = pi * (ang / 180)
    a = (s/2) * tan(ang)
    r = (s/2) * (1/(cos(ang)))
    Ac = pi * (r**2)
    an = pi * (180 / n)
    l = (cos(an)) / sin(an)
    Ap = (n * (s**2) * (l)) / 4
    print(Ac - Ap)