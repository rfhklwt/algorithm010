#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dic = collections.defaultdict(list)
        for i, c in enumerate(s):
            s_dic[c].append(i)
        t_dic = collections.defaultdict(list)
        for i, c in enumerate(t):
            t_dic[c].append(i)
        return list(s_dic.values()) == list(t_dic.values())


# @lc code=end
