# -*- coding: utf-8 -*-
"""
create time : 2018-03-21 20:30:21
author : sk


"""

# -*- coding: utf-8 -*-
"""
create time : 2018-03-21 17:15:59
author : sk


"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        f1 = nums[0]
        f2 = max(nums[0], nums[1])

        for n in nums[2:]:
            f = max(f2, f1+n)
            f1 = f2
            f2 = f
        return f2

if __name__ == '__main__':
    # nums = [8,9,100,5,6,7]
    nums = [2, 1, 1, 2]
    solution = Solution()
    result = solution.rob(nums)
    print(result)
