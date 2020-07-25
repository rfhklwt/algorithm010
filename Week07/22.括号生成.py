#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # dfs
        def backtrace(p, left, right, res=[]):
            if not right:
                res.append(p)
            else:
                if left:
                    backtrace(p + '(', left - 1, right)
                if right > left:
                    backtrace(p + ')', left, right - 1)
            return res
        return backtrace('', n, n)

# @lc code=end

