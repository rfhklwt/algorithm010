#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrace(p, xy_diff, xy_sum, res=[]):
            # 迭代的层数是行， 记录的数值是列
            row = len(p)
            if len(p) == n:
                res.append(p)
            else:
                for col in range(n):
                    if col not in p and col - row not in xy_diff and row + col not in xy_sum:
                        backtrace(p + [col], xy_diff + [col - row], xy_sum + [row + col])
            return res
        result = backtrace([], [], [])
        return [["."*i + "Q" + "."* (n - i - 1) for i in sol] for sol in result]
# @lc code=end

