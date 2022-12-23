#Next Greater Element I
# Solved using hashmap

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        for i in range(len(nums1)):
            b = True
            x = nums2.index(nums1[i])
            for j in range(x,len(nums2)):
                if nums1[i] < nums2[j]:
                    nums1[i] = nums2[j]
                    b = False
                    break
            if b:
                nums1[i] =-1
        
        return nums1
