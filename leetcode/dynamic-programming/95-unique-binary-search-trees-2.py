# -*- coding: utf-8 -*-
"""
create time : 2018-03-18 20:26:37
author : sk


"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def get_tree_json(self):
        if self.left is not None and self.right is not None:
            return {str(self.val):{'left':self.left.get_tree_json(), 'right':self.right.get_tree_json()}}
        elif self.left is not None:
            return {str(self.val):{'left':self.left.get_tree_json()}}
        elif self.right is not None:
            return {str(self.val):{'right':self.right.get_tree_json()}}
        else:
            return str(self.val)

    def __repr__(self):
        return str(self.val)

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        if n == 0:
            return []

        tree_node_list = []
        tree_node_list.append([None])
        tree_node_list.append([TreeNode(1)])
        
        for i in range(2, n+1):
            tree_node_list.append([])
            for j in range(1, i+1):
                for left_node in tree_node_list[j-1]:
                    for right_node in tree_node_list[i-j]:
                        root = TreeNode(j)
                        root.left = left_node
                        root.right = self.update_index(right_node, j)
                        tree_node_list[-1].append(root)
                        
        return tree_node_list[n]

    def update_index(self, tree_node, index):
        
        if tree_node is None:
            return None

        res = TreeNode(tree_node.val+index)
        res.left = self.update_index(tree_node.left, index)
        res.right = self.update_index(tree_node.right, index)

        return res

if __name__ == '__main__':
    solution = Solution()
    result = solution.generateTrees(3)
    
    for item in result:
        print(item.get_tree_json())

