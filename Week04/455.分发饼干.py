#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # T = O(nlogn)
        g.sort()
        s.sort()
        cookie, kid = 0, 0
        while cookie < len(s) and kid < len(g):
            if g[kid] <= s[cookie]:
                kid += 1
            cookie += 1
        return kid


# @lc code=end

