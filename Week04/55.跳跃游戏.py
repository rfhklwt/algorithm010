#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # T = O(N)
        # S = O(1)
        max_distance = 0
        for i,c in enumerate(nums):
            if i > max_distance:
                return False
            max_distance = max(max_distance, i + c)
        return True
# @lc code=end

