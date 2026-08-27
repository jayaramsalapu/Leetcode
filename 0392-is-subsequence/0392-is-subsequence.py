class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        indx = 0
        for i in t:
            if indx < len(s)  and i == s[indx]:
                indx+=1
        if indx>=len(s):
            return True
        else:
            return False