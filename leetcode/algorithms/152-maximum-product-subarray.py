# -*- coding: utf-8 -*-
"""
create time : 2018-03-20 21:57:54
author : sk


"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_list = []; max_list.append(nums[0])
        min_list = []; min_list.append(nums[0])
        res = nums[0]

        for item in nums[1:]:
            max_value = max(item, max_list[-1]*item, min_list[-1]*item)
            min_value = min(item, max_list[-1]*item, min_list[-1]*item)

            max_list.append(max_value)
            min_list.append(min_value)

            res = max(res, max_value)

        return res
