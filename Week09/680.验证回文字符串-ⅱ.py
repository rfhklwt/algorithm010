#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]: return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                new_s1 = s[:left] + s[left + 1:]
                new_s2 = s[:right] + s[right + 1:]
                return new_s1 == new_s1[::-1] or new_s2 == new_s2[::-1]
# @lc code=end
