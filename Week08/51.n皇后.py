#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrace(p, xy_sum, xy_diff, res=[]):
            row = len(p)
            if row == n:
                res.append(p)
            else:
                for col in range(n):
                    if col not in p and row + col not in xy_sum and row - col not in xy_diff:
                        backtrace(p + [col], xy_sum + [row + col], xy_diff + [row - col])
            return res
        res = backtrace([], [], [])
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in solution] for solution in res]
# @lc code=end

