#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     # 递归法
    #     res = []
    #     return self.helper(root, res)

    # def helper(self, root: TreeNode, res: List[int]) -> List[int]:
    #     if root:
    #         self.helper(root.left, res)
    #         res.append(root.val)
    #         self.helper(root.right, res)
    #     return res

        # 迭代法
        WHITE, GRAY = 0, 1
        stack = [(WHITE, root)]
        res = []
        while stack:
            color, node = stack.pop()
            if node:
                if color == WHITE:
                    stack.append((WHITE, node.right))
                    stack.append((GRAY, node))
                    stack.append((WHITE, node.left))
                else:
                    res.append(node.val)
        return res

# @lc code=end

