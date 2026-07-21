import math

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = []
        right = []
        res = []
        left_prod = 1
        right_prod =1
        for i in range(len(nums)):
            left_prod*=nums[i]
            left.append(left_prod)
        for i in range(len(nums)-1,-1,-1):
            right_prod*=nums[i]
            right.append(right_prod) 
        right.reverse()
        for i in range(len(nums)):
            if i==0:
                ans = right[i+1]
            elif i==len(nums)-1:
                ans = left[i-1]
            else:
                ans = left[i-1]*right[i+1]
            res.append(ans)
        return res
        