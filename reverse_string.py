class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        Time Complexity:
        ( O(n) ) — iterate through half of the array.
        Space Complexity:
        ( O(1) ) — in-place with no extra space used.
        """
        left,right=0,len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        
