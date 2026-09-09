class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq = {}

        for i in nums:
            freq[i] = freq.get(i,0)+1

        return sorted(freq,key=freq.get,reverse=True)[:k]
        