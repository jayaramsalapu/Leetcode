
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        total = 0
        max_sum = 0
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]]= freq.get(nums[i],0)+1
            total+=nums[i]

            while i-left+1>k:
                total-=nums[left]
                freq[nums[left]]-=1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left+=1


            if len(freq) == k :
                max_sum = max(max_sum,total)

        return max_sum
