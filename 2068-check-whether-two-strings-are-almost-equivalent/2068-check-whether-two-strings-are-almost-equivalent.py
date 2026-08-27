class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        freq1 = {}
        freq2 = {}
        for i in word1:
            freq1[i] = freq1.get(i,0)+1
        for i in word2:
            freq2[i] = freq2.get(i,0)+1

        for ch in set(word1+word2):
            if abs(freq1.get(ch,0)-freq2.get(ch,0))>3:
                return False
        
        return True
