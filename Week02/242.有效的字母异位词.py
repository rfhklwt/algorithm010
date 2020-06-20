#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    import collections
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        dic1 = collections.Counter(s)
        dic2 = collections.Counter(t)
        for word in s:
            if word not in dic2:
                return False
            if dic1[word] != dic2[word]:
                return False
        return True
# @lc code=end

