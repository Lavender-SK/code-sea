# -*- coding: utf-8 -*-
"""
create time : 2018-04-02 20:03:07
author : sk


"""

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 边界条件
        if len(nums) <= 1:
            return len(nums)

        # 动态规划,递推公式
        dp = [1] * len(nums)
        result_value = 0
        for (index, value) in enumerate(dp):
            tmp = [ dp[j]+1 for j in range(index) if nums[j]<nums[index]]
            tmp.append(value)
            dp[index] = max(tmp)
            result_value = max(dp[index], result_value)
        return result_value

if __name__ == '__main__':
        solution = Solution()
        # nums = [4,10,4,3,8,9]
        nums = [10,9,2,5,3,7,101,18]
        # nums = [1,3,6,7,9,4,10,5,6]
        result = solution.lengthOfLIS(nums)
        print(result)

