#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        strs = list(s)
        for i in range(0, len(strs), 2*k):
            strs[i: i + k] = reversed(strs[i: i + k])
        return ''.join(strs)


# @lc code=end

