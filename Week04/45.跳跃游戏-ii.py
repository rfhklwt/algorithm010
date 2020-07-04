#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # T = O(n)
        # S = O(1)
        if len(nums) <= 1: return 0
        start, end = 0, nums[0]
        count = 0
        while end < len(nums) - 1:
            start, end = end, max(i + nums[i] for i in range(start, end + 1))
            count += 1
        return count + 1
# @lc code=end

