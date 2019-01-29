# -*- coding: utf-8 -*-
"""
create time : 2018-04-02 21:25:37
author : sk


"""

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [float('inf')] * (n+1)

        # 初始化各个完美平方数
        i = 1
        while i*i < n+1:
            dp[i*i] = 1
            i += 1

        # 动态规划, 遍历递推公式
        # dp[i+j*j] = min(dp[i]+1, dp[i+j*j])
        for i in range(1,n+1):
            j = 1 # 选定一个完美平方数
            while i+j*j <= n:
                dp[i+j*j] = min(dp[i+j*j], dp[i]+1)
                j += 1

        # 返回结果
        # print(dp) 
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    n = 12
    result = solution.numSquares(n)
    print('result:\t', result)

