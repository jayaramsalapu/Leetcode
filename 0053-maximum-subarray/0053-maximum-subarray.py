class Solution(object):
    def maxSubArray(self, nums):

        sums = 0
        maxi = nums[0]
        for i in range(len(nums)):
            sums+=nums[i]
            maxi = max(maxi,sums)
            if sums<0:
                sums=0
            
        return maxi
