#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:
    # 递归版本
    #    res = []
    #    return self.helper(root, res)

    # def helper(self, root: 'Node', res: List[int]) -> List[int]:
    #    if root:
    #        res.append(root.val)
    #        for child in root.children:
    #            self.helper(child, res)
    #    return res
    # 迭代版本
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.extend(node.children[::-1])
        return res





# @lc code=end

