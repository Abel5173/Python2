# from array import array

# arr = array('i',[1,2,3,4,5])
# print(arr)

# dist = lambda p1, p2: sum((a - b) * (a - b) for a, b in zip(p1, p2))**0.5

# perimeter = lambda *p: sum(dist(i, j) for i, j in zip(p, p[1:] + p[:1]))

# area = lambda *p: abs(sum(i[0] * j[1] - j[0] * i[1] for i, j in zip(p, p[1:] + p[:1]))) / 2

# is_in_circle = lambda p, c, r: sum(i * i - j * j for i, j in zip(p, c)) < r * r

# incircle_radius = lambda a, b, c: area(a, b, c) / (perimeter(a, b, c) / 2)

# circumcircle_radius = lambda a, b, c: (dist(a, b) * dist(b, c) * dist(c, a)) / (4 * area(a, b, c))
from math import gcd


def reflection_of_point(p, q_i, q_j):

    b = q_j[1] - q_i[1]
    a = q_j[0] - q_i[0]
    if b == 0:
        p_k = [(2*a - p[0]), p[1]]
    elif a == 0:
        p_k = [p[0], (2*b - p[1])]
    else:
        g = gcd(a, b)
        m = [(a//g), (b//g)]
        c = (q_j[0]*q_j[1]-q_i[0]*q_j[1])/(q_j[0]-q_i[0])
        d = (p[0] + (p[1] - c)*m)/(1 + m**2)
        p_k = [(2*d - p[0]), 2*d*m - p[1] + 2*c]
    return p_k


p = [4, 7]
a = [1, 3]
b = [3, 3]
print(reflection_of_point(p, a, b))
