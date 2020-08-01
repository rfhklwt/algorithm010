#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            # 取出最右边一位，并左移power位
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret


# @lc code=end

