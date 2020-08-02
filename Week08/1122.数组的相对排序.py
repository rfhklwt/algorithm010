#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res, count = [], collections.Counter(arr1)
        for i in arr2:
            if count[i]:
                res.extend([i] * count.pop(i))
        # 剩下的数组
        left = sorted(list(count.items()), key=lambda x: x[0])
        for num, time in left:
            res.extend([num] * time)
        return res

# @lc code=end
