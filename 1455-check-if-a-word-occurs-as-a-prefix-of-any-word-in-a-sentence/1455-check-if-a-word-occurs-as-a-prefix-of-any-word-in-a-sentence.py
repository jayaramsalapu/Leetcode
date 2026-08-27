class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        sentence = sentence.split()
        for word in range(len(sentence)):
            if sentence[word].startswith(searchWord):
                return word+1
                break
        
        return -1
            