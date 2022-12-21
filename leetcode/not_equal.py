nums = [int(i) for i in input().split()]

nums.sort()
res = []
l,  r = 0, len(nums) - 1

while len(res) != len(nums):
    res.append(nums[l])
    l += 1

    if l <= r:
        res.append(nums[r])
        r -= 1

print(*res)