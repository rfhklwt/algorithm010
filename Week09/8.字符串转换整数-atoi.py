#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        num = list(str.strip())
        if not num: return 0
        # 求符号
        sign = -1 if num[0] == '-' else 1
        if num[0] in ['-', '+']: del num[0]
        ret, i = 0, 0
        while i < len(num) and num[i].isdigit():
            ret = ret * 10 + ord(num[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))

# @lc code=end

