n = int(input())
l = [int(i) for i in input().split()]
cnt = 0
for i in range(0, n):
    for j in range(0, n-1):
        if l[j]>l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
            cnt +=1

print(f'Array is sorted in {cnt} swaps.')
print(f'First Element: {l[0]}')
print(f'Last Element: {l[-1]}')