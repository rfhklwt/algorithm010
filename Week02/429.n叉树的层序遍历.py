#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    import collections
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        stack = [root]
        while any(stack):
            res.append([node.val for node in stack])
            stack = [child for node in stack for child in node.children if child]
        return res


# @lc code=end

