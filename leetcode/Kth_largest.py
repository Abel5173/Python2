nums = [i for i in input().split()]
k = int(input())
nums = [int(i) for i in nums]
nums.sort(reverse=True)
print(nums)
print(nums[k-1])