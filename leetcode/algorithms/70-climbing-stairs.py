# -*- coding: utf-8 -*-
"""
create time : 2018-04-03 21:30:37
author : sk


"""

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 1:
            return 1

        # 动态规划 遍历递推公式
        dp = [1,1]
        for i in range(2,n+1):
            dp.append(dp[-1]+dp[-2])
        
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    n = 4  
    result = solution.climbStairs(n)
    print(result)
