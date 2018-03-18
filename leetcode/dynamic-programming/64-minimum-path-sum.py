# -*- coding: utf-8 -*-
"""
create time : 2018-03-18 20:34:59
author : sk


"""

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # 获取行数和列数
        h = len(grid)
        w = len(grid[0])

        # 遍历
        for i in range(1,h):
            grid[i][0] = grid[i-1][0] + grid[i][0]

        for i in range(1, w):
            grid[0][i] = grid[0][i-1] + grid[0][i]

        for i in range(1,h):
            for j in range(1,w):
                grid[i][j] = min(grid[i-1][j]+grid[i][j], grid[i][j-1]+grid[i][j])

        return grid[h-1][w-1]

if __name__ == '__main__':
    grid = [[1,3,1],
            [1,5,1],
            [4,2,1]]

    solution = Solution()
    print(solution.minPathSum(grid))

