nums = [int(i) for i in input().split()]

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        a = int(''.join([str(nums[i]), str(nums[j])]))
        b = int(''.join([str(nums[j]), str(nums[i])]))
        if b > a:
            nums[i], nums[j] = nums[j], nums[i]
s = ''.join(map(str, nums))
print(s)
