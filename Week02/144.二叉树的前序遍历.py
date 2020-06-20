#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    import collections
    def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     # 递归
    #     res = []
    #     return self.helper(root, res)

    # def helper(self, root: TreeNode, res: List[int]) -> List[int]:
    #     if root:
    #         res.append(root.val)
    #         self.helper(root.left, res)
    #         self.helper(root.right, res)
    #     return res
        # 迭代
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res


# @lc code=end

