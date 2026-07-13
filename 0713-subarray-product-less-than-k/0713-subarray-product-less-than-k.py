class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for right in range(len(nums)):
            prod = 1
            left = right
            while(left<len(nums)):
                prod *= nums[left]
                if prod >= k:
                    break
                else: 
                    count+=1
                    left+=1
        return count
                