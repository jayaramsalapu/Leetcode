class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = 0 

        for i in s:
            result ^= ord(i)

        for i in t:
            result ^= ord(i)

        return chr(result)