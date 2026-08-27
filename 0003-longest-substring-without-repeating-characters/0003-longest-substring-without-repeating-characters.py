class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = set()
        left = 0
        ans = 0
        for right in range(len(s)):
            while s[right] in used:
                used.remove(s[left])
                left+=1
            
            used.add(s[right])
            ans = max(ans,right-left+1)
        return ans   