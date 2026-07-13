class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        sums=0
        min_count = float('inf')
        for right in range(len(nums)):            
            sums+=nums[right]

            while sums>=target:
                min_count=min(min_count,right-left+1)
                sums-=nums[left]
                left+=1
                

        return 0 if min_count == float('inf') else min_count
                