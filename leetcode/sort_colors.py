l = [int(i) for i in input().split()]
x = []
for i in range(len(l)):
    min_idx = i
    for j in range(i+1,len(l)):
        if l[min_idx] > l[j]:
            min_idx = j
    l[i], l[min_idx] = l[min_idx], l[i]
print(l)