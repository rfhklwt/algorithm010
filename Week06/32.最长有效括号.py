#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 方法：栈（用动态递归面试肯定会忘记）
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                # 假如stack为空，说明现在这个匹配不了，故放进去充当-1
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res
# @lc code=end

