#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # 把这道题想象成爬楼梯
        # dp[i]表示字符串0到i - 1的解码方法有多少
        # dp[i] = dp[i - 1] + dp[i - 2] if '10' <= s[i - 2: i] <= '26'
        # base case
        # dp[0] = 1
        # dp[1] = 1 if s[0] != '0' else 0
        n = len(s)
        if n == 0 or s[0] == '0': return 0
        elif n == 1: return 1
        dp = [1] + [0] * n
        # 对于第一个字符
        dp[1] = 1 if s[1] != '0' else 0
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            if '10' <= s[i - 2: i] <= '26':
                dp[i] += dp[i - 2]
        return dp[-1]

# @lc code=end

