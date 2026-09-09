class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1

        return max(freq,key=freq.get)
        