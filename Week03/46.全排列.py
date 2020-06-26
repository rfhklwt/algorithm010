#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # # 1. 递归回溯
        # def backtrace(p, new_nums, res=[]):
        #     if len(new_nums) == 0:
        #         res.append(p)
        #     else:
        #         for i, c in enumerate(new_nums):
        #             backtrace(p + [c], new_nums[:i] + new_nums[i + 1:])
        #     return res
        # return backtrace([], nums)
        # 2. 插队法
        res = [[]]
        # 对于每一个要插入的数
        for n in nums:
            p = []
            for ele in res:
                for i in range(len(ele) + 1):
                    p.append(ele[:i] + [n] + ele[i:])
            res = p
        return res


# @lc code=end

