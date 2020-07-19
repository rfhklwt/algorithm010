#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        ball = [1] + nums + [1]
        @lru_cache(None)
        # 求出(left, right)获得最大的硬币量
        def solve(left, right):
            # 区间不存在，返回
            if left + 1 == right:
                return 0
            # 区间存在
            # i是介于left + 1到right之间，左开右闭
            best = 0
            for i in range(left + 1, right):
                total = ball[left] * ball[i] * ball[right]
                total += solve(left, i) + solve(i, right)
                best = max(best, total)
            return best
        return solve(0, len(nums) + 1)
# @lc code=end

