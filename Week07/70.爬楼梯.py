#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
# 找规律
# f(1): 1
# f(2): 2
# f(3): f(1) + f(2)
# f(4): f(2) + f(3)
# f(n): f(n - 1) + f(n)
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return b

# @lc code=end

