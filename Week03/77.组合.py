#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrace(p, start, k, res=[]):
            if len(p) == k:
                res.append(p)
            else:
                for i in range(start, n - (k - len(p)) + 2):
                    backtrace(p + [i], i + 1, k)
            return res
        return backtrace([], 1, k)

# @lc code=end

