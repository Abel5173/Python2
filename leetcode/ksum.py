# l = [1,3,4,3,5,3]
from collections import defaultdict

l = [3,1,3,4,3]
k = 6
hash = defaultdict(int)
cnt = 0 

for num in l:
    target = k - num
    
    if hash[target] > 0:
        hash[target] -= 1
        cnt += 1
    else:
        hash[num] += 1
print(cnt)