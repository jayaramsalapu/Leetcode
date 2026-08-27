class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s)!=len(t):
            return False

        freq = {}

        for i in s:
            freq[i] = freq.get(i,0)+1

        for i in t:

            if i not in freq or freq[i]==0:
                return False

            freq[i]-=1
            
        return True