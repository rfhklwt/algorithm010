#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid[0]
        # 初始化第一行
        for i in range(1, len(grid[0])):
            dp[i] += dp[i - 1]
        # 一行一行遍历(从第二行开始)
        for i in range(1, len(grid)):
            # 一列一列遍历
            for j in range(len(grid[0])):
                if j == 0:
                    dp[j] = dp[j] + grid[i][0]
                else:
                    dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
        return dp[-1]


# @lc code=end

