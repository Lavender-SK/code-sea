# -*- coding: utf-8 -*-
"""
create time : 2018-04-07 21:54:59
author : sk


"""

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        if len(cost) == 0:
            return 0
        if len(cost) <= 2:
            return min(cost)

        dp = [cost[0], cost[1]]

        for c in cost[2:]:
            dp.append(min(dp[-1]+c, dp[-2]+c))
        return min(dp[-1], dp[-2])

if __name__ == '__main__' :
    solution = Solution()
    # cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    cost = [10, 15, 20]
    result = solution.minCostClimbingStairs(cost)
    print(result)


