#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        left, right = 0, len(S) - 1
        S = list(S)
        while left < right:
            if S[left].isalpha() and S[right].isalpha():
                S[left], S[right] = S[right], S[left]
                left += 1
                right -= 1
            elif S[left].isalpha():
                right -= 1
            else:
                left += 1
        return ''.join(S)

# @lc code=end
