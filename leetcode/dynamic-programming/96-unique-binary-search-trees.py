# -*- coding: utf-8 -*-
"""
create time : 2018-03-18 20:28:58
author : sk


"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        L = [1, 1]

        for i in range(2, n+1):
            L.append(0)
            for j in range(1, i+1):
                L[i] += L[j-1] * L[i-j]

        return L[-1]


if __name__ == '__main__':
    solution = Solution()
    result = solution.numTrees(2)
    print(result)
