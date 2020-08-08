#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] 表示s[0: i - 1]中t[0: j - 1]出现的个数
        # dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] if s[i - 1] == t[j - 1]
        # dp[i][j] = dp[i - 1][j] if s[i - 1] != t[j - 1]
        # base case
        # dp[:][0] = 1
        m, n = len(s) + 1, len(t) + 1

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] * (s[i - 1] == t[j - 1])
        return dp[-1][-1]




# @lc code=end
