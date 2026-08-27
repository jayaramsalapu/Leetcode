class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        even = 0
        odd = 0

        for i in range(len(num)):
            if i % 2 != 0:
                odd+=int(num[i])
            else:
                even+=int(num[i])
        if odd == even:
            return True
        else:
            return False