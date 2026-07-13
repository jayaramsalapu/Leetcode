class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        s=0
        m = float('inf')
        for r in range(len(nums)):            
            s+=nums[r]

            while s>=target:
                m=min(m,r-l+1)
                s-=nums[l]
                l+=1
                

        return 0 if m == float('inf') else m
                