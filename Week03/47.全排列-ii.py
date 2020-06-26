#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrace(p, new_nums, res=[]):
            if not new_nums:
                res.append(p)
            else:
                visited = set()
                for i, c in enumerate(new_nums):
                    if c in visited: continue
                    else:
                        backtrace(p + [c], new_nums[:i] + new_nums[i + 1:])
                    visited.add(c)
            return res
        return backtrace([], nums)


# @lc code=end

