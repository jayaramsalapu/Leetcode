class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd = False
        freq = {}
        for i in s:
            freq[i] = freq.get(i,0)+1

        length = 0
        for i in freq.values():
            length += (i//2)*2

            if i%2==1:
                odd = True

        if odd:
            length+=1
            
        return length
        