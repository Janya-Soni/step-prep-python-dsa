class Solution(object):
    def fib(self, n):
        """
        DYNAMIC VERSION
        :type n: int
        :rtype: int
        we return f1 because fnext is a temporary variable
        """
        f0=0
        f1=1
        if n<=0:
            return 0
        if  n==2 or n==1:
            return 1
        for i in range(2,n+1):
            fnext=f0+f1
            f0,f1=f1,fnext
        return f1

        