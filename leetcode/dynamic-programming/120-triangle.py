# -*- coding: utf-8 -*-
"""
create time : 2018-03-18 20:46:34
author : sk


"""

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        result = triangle[-1]
        for i in reversed(range(len(triangle)-1)):
            print(result)
            for j in range(len(triangle[i])):
                result[j] = min(result[j]+triangle[i][j],
                        result[j+1]+triangle[i][j])
        return result[0]

        
if __name__ == '__main__':
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    solution = Solution()
    result = solution.minimumTotal(triangle)
    print(result)
