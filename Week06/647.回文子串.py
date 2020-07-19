#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        N = len(s)
        for center in range(2 * N - 1):
            # 当center在字符串上，那left也在字符串，当在字符串的缝隙，那left在缝隙的左边
            left = center // 2
            # # 当center在字符串上，那right也在字符串，当在字符串的缝隙，那right在缝隙的右边
            right = left + center % 2
            while left >= 0 and right <= N - 1 and s[left] == s[right]:
                res += 1
                # 两边扩散
                left -= 1
                right += 1
        return res


# @lc code=end

