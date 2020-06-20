#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    import collections
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # 方法一
        # if k == len(nums): return nums
        # count = collections.Counter(nums)
        # return [item[0] for item in count.most_common(k)]

        # 方法二
        f_dic = collections.defaultdict(list)
        res = []
        biggest = 0
        for num, freq in collections.Counter(nums).items():
            f_dic[freq].append(num)
            # 存储最大的频次
            biggest = max(biggest, freq)
        for time in range(biggest, 0, -1):
            res.extend(f_dic[time])
            if len(res) >= k: break
        return res if len(res) == k else res[:k]






# @lc code=end

