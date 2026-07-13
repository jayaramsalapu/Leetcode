class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        zeros = []
        max_count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros.append(right)
                
            if len(zeros)>k:
                left = zeros.pop(0)+1
                
            max_count = max(max_count,right-left+1)
        return max_count

                