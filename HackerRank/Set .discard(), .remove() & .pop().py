n = int(input())
l = set([int(i) for i in input().split()])
N = int(input())
for i in range(N):
    li = [i for i in input().split()]
    l.discard(int(b))
print(sum(list(l)))