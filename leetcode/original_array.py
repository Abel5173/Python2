from collections import Counter

changed = [int(i) for i in input().split()]

n = len(changed)
if n % 2:
    print('[]')

count = Counter(changed)
changed.sort()
ans = []

for num in changed:
    if num == 0 and count[num] >= 2:
        count[num] -= 2
        ans.append(num)
    elif num > 0 and count[num] and count[num*2]:
        count[num] -= 1
        count[num*2] -= 1
        ans.append(num)

print(ans if len(ans) == n // 2 else [])