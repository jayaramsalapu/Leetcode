class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        freq = [0] * 26

        for ch in magazine:
            freq[ord(ch)-ord('a')]+=1

        for ch in ransomNote:
            index = ord(ch) - ord('a')

            if freq[index] == 0:
                return False

            freq[index] -=1

        return True
            