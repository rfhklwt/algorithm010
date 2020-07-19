#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        #dp[i] = dp[i - 1] + dp[i - 2] if int(s[i - 1:]) < 26
        # 字符串只有1个的时候
        if not s or s[0] == '0': return 0
        if len(s) == 1: return 1
        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            # 单个解码
            if s[i] != '0':
                dp[i] = dp[i - 1]
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        return dp[-1]


# @lc code=end

