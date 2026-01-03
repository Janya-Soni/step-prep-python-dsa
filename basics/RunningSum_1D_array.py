class Solution(object):
    def runningSum(self, nums):
        lt=[]
        s=0
        for i in nums:
            s+=i            
            lt.append(s)
        return lt
        