class Solution(object):
    def maximumWealth(self, accounts):
        acc_sum=0
        for i in accounts:
            cus_wth=0
            for j in i:
                cus_wth+=j
            if cus_wth>acc_sum:
                acc_sum=cus_wth
        return acc_sum
        