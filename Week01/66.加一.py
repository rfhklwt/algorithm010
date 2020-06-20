#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            digits[i] += 1
            if digits[i] <= 9: return digits
            else:
                digits[i] = 0
            i -= 1
        if digits[0] == 0:
            new_digits = [1] + digits[:]
            return new_digits
# @lc code=end

