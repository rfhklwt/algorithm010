#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = []
        # 初始化window，起始索引为0
        res = []
        n = len(p)
        target = collections.Counter(p)
        window = collections.Counter(s[:n])
        for i in range(0, len(s)):
            if window == target:
                res.append(i)
            # 更新window
            # 更新左边界
            window[s[i]] -= 1
            if window[s[i]] == 0:
                del window[s[i]]
            # 更新右边界
            if i + n < len(s):
                window[s[i + n]] = window.get(s[i + n], 0) + 1
        return res




# @lc code=end
