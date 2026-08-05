class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p)>len(s):
            return []
        
        p_count = [0]*26
        s_count = [0]*26

        for ch in p:
            p_count[ord(ch)-ord('a')]+=1     

        result = []
        left = 0
        for right in range(len(s)):
            s_count[ord(s[right])-ord('a')]+=1

            if right - left +1 > len(p):
                s_count[ord(s[left])-ord('a')]-=1
                left+=1 

            if s_count == p_count:
                result.append(left)
        return result