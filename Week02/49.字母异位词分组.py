#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    import collections
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        # 对于异位词，他们的的key值应该相等
        # 通过tuple(sorted(word))的方式可以实现
        for word in strs:
            key = tuple(sorted(word))
            res[key].append(word)
        return list(res.values())
# @lc code=end

