class Solution(object):
    from collections import Counter
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        frq=Counter(s)
        for index,ch in enumerate(s):
            if frq[ch]==1:
                return index
        return -1

        

