class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        count = 0
        for word in range(left,right+1):
            if words[word][0] in "aieou" and words[word][-1] in "aeiou":
                count+=1

        return count
        