# -*- coding: utf-8 -*-
"""
create time : 2018-03-20 22:11:58
author : sk


"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_list = []
        max_list.append(nums[0])
        res = nums[0]

        for item in nums[1:]:
        	max_value = max(item, max_list[-1]+item)
        	max_list.append(max_value)
        	
        	res = max(res, max_list[-1])	
        
        return res
		

if __name__ == '__main__':
	solution = Solution()
	nums = [-2,1,-3,4,-1,2,1,-5,4]
	result = solution.maxSubArray(nums)
	print(result)


