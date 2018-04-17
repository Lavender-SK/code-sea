# -*- coding: utf-8 -*-
"""
create time : 2018-04-15 20:48:20
author : sk


"""

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        width = len(word1)
        height = len(word2)

        if width == 0:
            return height
        if height == 0:
            return width

        old_list = range(width+1)

        for h in range(1, height+1):
            new_list = [h] 
            for w in range(1, width+1):
                if word2[h-1] == word1[w-1]:
                    new_list.append(old_list[w-1])
                else:
                    new_list.append(min(old_list[w-1]+1, old_list[w]+1, new_list[-1]+1))
            old_list = new_list

        return old_list[-1]


if __name__ == '__main__':
    solution = Solution()
    #word1 = 'ab'
    #word2= 'a'
    word1 = "plasma"
    word2 = "altruism"
    result = solution.minDistance(word1, word2)
    print(result)
